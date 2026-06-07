from pypylon import pylon
import cv2
import numpy as np
import snap7
from snap7.util import set_int, set_bool, get_bool
import time

# --- CONFIGURATION SIEMENS S7-1500 ---
PLC_IP = "172.16.1.101"
DB_NUMBER = 39
plc = snap7.client.Client()

# --- COEFFICIENTS DE CALIBRATION (PIXELS -> MM) ---
# À ajuster lors de tes tests en mode Initialisation
COEFF_X = 0.5      
OFFSET_X = -300.0  
COEFF_Y = 0.5
OFFSET_Y = 150.0

try:
    plc.connect(PLC_IP, 0, 1)
    print("Connecté à l'automate avec succès.")
except Exception as e:
    print(f"Impossible de se connecter à l'automate : {e}")

try:
    # Initialisation de la caméra Basler
    factory = pylon.TlFactory.GetInstance()
    devices = factory.EnumerateDevices()
    if not devices:
        raise RuntimeError("Aucune caméra détectée !")

    camera = pylon.InstantCamera(factory.CreateDevice(devices[0]))
    camera.Open()
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    
    # Convertisseur pour OpenCV (BGR)
    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed

    print("Système de vision prêt. En attente du signal automate...")

    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            frame = image.GetArray()

            # Lecture des bits de contrôle de l'automate (Octet 6)
            if plc.get_connected():
                db_status = plc.db_read(DB_NUMBER, 6, 1)
                trigger_plc = get_bool(db_status, 0, 0)     # 6.0 : Trigger_Vision
                mode_init = get_bool(db_status, 0, 2)       # 6.2 : Mode_Init
            else:
                trigger_plc = False
                mode_init = False

            # Traitement d'image si Trigger actif ou si on est en Mode Init
            if trigger_plc or mode_init:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (11, 11), 0)
                _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)
                
                contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                for cnt in contours:
                    if cv2.contourArea(cnt) > 5000:  # Filtre de taille de l'objet
                        rect = cv2.minAreaRect(cnt)
                        (cx, cy), (w, h), angle = rect
                        
                        # 1. Conversion des Pixels en Millimètres (Repère Robot)
                        mm_x = (cx * COEFF_X) + OFFSET_X
                        mm_y = (cy * COEFF_Y) + OFFSET_Y
                        mm_angle = angle

                        # 2. Application du facteur 10 pour intégrer la décimale dans l'entier
                        val_x = int(round(mm_x * 10))
                        val_y = int(round(mm_y * 10))
                        val_angle = int(round(mm_angle * 10))

                        # 3. Extraction du signe (0 = Positif, 1 = Négatif)
                        signe_x = 1 if val_x < 0 else 0
                        signe_y = 1 if val_y < 0 else 0
                        signe_angle = 1 if val_angle < 0 else 0

                        # 4. Restriction à la valeur absolue sur 12 bits max (0 à 4095)
                        abs_x = min(abs(val_x), 4095)
                        abs_y = min(abs(val_y), 4095)
                        abs_angle = min(abs(val_angle), 4095)

                        # Visuels de tracking à l'écran
                        cv2.circle(frame, (int(cx), int(cy)), 7, (0, 255, 0), -1)
                        if mode_init:
                            cv2.putText(frame, f"MODE INIT - PX X:{int(cx)} Y:{int(cy)}", (30, 50), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 140, 255), 2)
                        else:
                            cv2.putText(frame, f"RUN - mm X:{abs_x/10} Y:{abs_y/10}", (30, 50), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                        # Envoi des données vers le DB39 de l'automate 
                        if plc.get_connected():
                            # Écriture des 3 valeurs absolues (X_Pixel, Y_Pixel, Angle sur les offsets 0, 2, 4)
                            buffer_values = bytearray(6)
                            set_int(buffer_values, 0, abs_x)
                            set_int(buffer_values, 2, abs_y)
                            set_int(buffer_values, 4, abs_angle)
                            plc.db_write(DB_NUMBER, 0, buffer_values)

                            # Écriture de l'octet 6 (Donnees_Pretes + les 3 Bits de signes)
                            status_byte = plc.db_read(DB_NUMBER, 6, 1)
                            set_bool(status_byte, 0, 1, True)          # 6.1 : Donnees_Pretes = True
                            set_bool(status_byte, 0, 3, bool(signe_x))  # 6.3 : Signe_X
                            set_bool(status_byte, 0, 4, bool(signe_y))  # 6.4 : Signe_Y
                            set_bool(status_byte, 0, 5, bool(signe_angle)) # 6.5 : Signe_Angle
                            plc.db_write(DB_NUMBER, 6, status_byte)

                            print(f"Données transmises -> X:{abs_x} (S:{signe_x}) | Y:{abs_y} (S:{signe_y}) | Ang:{abs_angle} (S:{signe_angle})")

                            # Handshake : On attend que l'automate traite la donnée et coupe le Trigger_Vision (6.0)
                            # Si on est en Mode_Init (6.2), on n'attend pas le handshake pour rafraîchir l'image en continu
                            if not mode_init:
                                while True:
                                    check = plc.db_read(DB_NUMBER, 6, 1)
                                    if not get_bool(check, 0, 0):  # Attend que Trigger_Vision repasse à False
                                        break
                                    time.sleep(0.01)

                                # Nettoyage : On coupe le bit Donnees_Pretes (6.1)
                                status_byte = plc.db_read(DB_NUMBER, 6, 1)
                                set_bool(status_byte, 0, 1, False)
                                plc.db_write(DB_NUMBER, 6, status_byte)
                        break  # On traite un seul objet principal par cycle

            # Affichage de la fenêtre d'analyse
            cv2.imshow('Analyse Vision Robotique Fanuc', cv2.resize(frame, (960, 540)))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        grabResult.Release()

finally:
    if plc.get_connected():
        plc.disconnect()
        print("Connexion automate fermée.")
    camera.Close()
    cv2.destroyAllWindows()