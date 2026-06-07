---
layout: default
nav_order: 5
parent: Réalisations
title: Réalisations logicielle
---

# Réalisations logicielle

Pour valider le comportement du système de vision et sa communication, une série d'essais a été réalisée dans la cellule et sur l'automate :

<img width="359" height="478" alt="image" src="https://github.com/user-attachments/assets/0a26b158-fc99-4072-b84c-c5e2f555ce24" />

Les premiers tests ont confirmé la communication avec la caméra Basler. Le script Python assure la récupération continue du flux vidéo en direct, rendant les images disponibles pour la phase de traitement.

<img width="472" height="250" alt="image" src="https://github.com/user-attachments/assets/6cee8379-e9ea-450d-bbb8-b35c20285c25" />

La réception du signal provenant du capteur de présence de la cellule a été validée. Dès que l'automate détecte un contenant, il transmet une instruction au script Python, ce qui déclenche la capture de l'image à analyser.

<img width="222" height="209" alt="image" src="https://github.com/user-attachments/assets/72728cda-fcc3-472f-817e-53928aab27ca" />

L'algorithme OpenCV traite l'image capturée. Le script isole le contenant, détermine ses coordonnées géométriques (X, Y) ainsi que son angle d'orientation, et les affiche sur le retour vidéo afin de permettre une vérification des valeurs en direct.

La dernière phase d'essais a validé la communication descendante. Les coordonnées calculées par Python sont transmises vers l'automate, qui les réceptionne et les stocke dans le bloc de données (DB) interne.

