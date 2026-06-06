---
layout: default
nav_order: 4
title: Conception détaillée
---

# Conception détaillée 

## Conception CAO

L'ensemble des modèles 3D des pièces suivantes est accessible directement sur notre espace Onshape, via le lien disponible sur la page d'accueil.


### Support caméra

<img width="945" height="730" alt="image" src="https://github.com/user-attachments/assets/be49ebae-39fb-4ee8-b278-f9183ab71503" />

Le support de la caméra a été modélisé pour s'adapter parfaitement aux profilés en aluminium de section 45 x 45 mm. Des vis M8 sont utilisées pour verrouiller solidement le support sur la structure, garantissant une stabilité mécanique et une résistance suffisante pour répondre aux contraintes de vibrations lors du fonctionnement du robot.

Les points de fixation inférieurs sont dimensionnés spécifiquement pour accueillir la caméra Basler ace 2 ainsi que son dissipateur thermique afin de garantir le refroidissement de la caméra. Grâce à cette géométrie, la caméra bénéficie d'une visée zénithale perpendiculaire au plan du convoyeur, ce qui lui permet de garantir la précision de l'analyse d'image.


### Equerres de fixation

<img width="939" height="661" alt="image" src="https://github.com/user-attachments/assets/592e0d5e-ee3a-4fd4-a64a-b4e7629bad2e" />

Afin de lier le profilé préalablement découpé à l'armature principale de la cellule de conditionnement, la modélisation d'équerres de fixation sur mesure de 45 x 45 mm s'est avérée nécessaire. Le laboratoire PAUC ne disposant pas d'équerres commerciales adaptées à nos contraintes géométriques et d'entraxe (prévues pour de la visserie M6), nous avons opté pour une approche de prototypage rapide.

Le modèle a été conçu sur Onshape et a permis de valider rapidement l'assemblage mécanique tout en garantissant la solidité du montage.


### Montage complet

<img width="939" height="725" alt="image" src="https://github.com/user-attachments/assets/44f232a6-c1fe-41ee-b6a7-635ce4969c12" />

Cette vue d'ensemble présente le montage complet, associant le support de la caméra et les équerres de fixation sur le profilé en aluminium sur mesure. Cette modélisation offre un aperçu fidèle de la configuration finale de notre solution.


### Support Raspberry

<img width="939" height="725" alt="image" src="https://github.com/user-attachments/assets/6fd3f118-8617-470c-a0f7-0abd4aa3591e" />

Ce modèle présente le support dédié au Raspberry Pi 5 que nous avons modélisé. Il assure la fixation entre le boîtier de la carte électronique et la structure de la cellule. La fixation du boîtier sur le support est réalisée via quatre vis M3, tandis que l'ancrage sur le profilé en aluminium s'effectue à l'aide d'inserts de diamètre M8.

La géométrie du support intègre des fentes d'aération positionnées pour optimiser le flux thermique. Cela permet de prévenir le risque de surchauffe lors des phases de traitement d'image intensives.


## Conception logicielle

### Programme Python

 <img width="351" height="351" alt="image" src="https://github.com/user-attachments/assets/705a6afc-229b-499d-aab2-a08b9bb1d7a0" />

Le script Python fait le pont entre le flux vidéo brut et l’automate. Son rôle est de transformer une matrice de pixels en coordonnées physiques, puis de les injecter dans la mémoire de l'automate.

**1.	Acquisition et traitement d’image**

<img width="289" height="138" alt="image" src="https://github.com/user-attachments/assets/672e9c66-d4b3-4151-b327-713431304139" />

Le programme utilise l'API du constructeur (protocole GigEVision) pour piloter la caméra Basler ACE. Dès la réception du signal de l’automate, le script déclenche une capture d'image.  

<img width="428" height="201" alt="image" src="https://github.com/user-attachments/assets/5b1a7573-fbee-4e24-9035-40392b43296a" />

La matrice brute obtenue est immédiatement convertie en niveaux de gris grâce à la bibliothèque OpenCV. Un filtrage par « seuillage binaire » est appliqué pour isoler le contenant de l’arrière-plan du convoyeur. L'algorithme extrait ensuite les contours de l'objet (via cv2.findContours) et applique une boîte englobante orientée (cv2.minAreaRect). Cette méthode permet d'extraire simultanément : le centre de gravité du contenant (X pixels,  Y pixels) et son inclinaison (Angle par rapport à l’axe horizontale).

 <img width="383" height="413" alt="image" src="https://github.com/user-attachments/assets/371aa119-de0d-49a0-a244-9e6fc5f2a49a" />

 
**2. Préparation et conversion des données**
   
Les coordonnées extraites étant exprimées en pixels, le script applique un facteur d'échelle (mm/pixel) déterminé par un étalonnage effectué au préalable. Cette opération permet de mettre les données sur la même unité de grandeur que le robot.

Pour garantir la lisibilité des informations pour le robot, les données sont ensuite converties :

- Les valeurs flottantes sont multipliées par un facteur de précision (ex:  10) puis converties en entiers (INT), car le robot ne peut pas lire de décimal et donc de nombre réel.
- Les signes des coordonnées (positifs ou négatifs) sont isolés et traduits sous forme de bits de polarité distincts, évitant ainsi les erreurs d'interprétation de signe.
  
**3. Communication avec l’automate**
   
La transmission finale repose sur la bibliothèque Snap7, qui émule un client de communication natif Siemens en TCP/IP. Le script Python structure les coordonnées et les bits de polarité sous forme de trame d'octets (16bits). Enfin, le programme utilise des requêtes d'écriture directes (db_write) pour injecter ces données directement dans un bloc de données de l'automate, afin que celui puisse les envoyés au robot FANUC.


### Programme Automate (PLC1)

  <img width="328" height="184" alt="image" src="https://github.com/user-attachments/assets/f6adb4e0-582c-4f9c-9d7b-3b34231f9d01" />

L'automate gère la lecture, la gestion et le transfert des données vers le robot. Configuré sous TIA Portal, il sert de passerelle entre le traitement informatique (Python) et l'action mécanique (Robot FANUC).

**1. Structuration et stockage des données**

Pour centraliser les informations issues du retour vidéo, l'automate utilise un bloc de données global dédié, appelé DB (Data Block). Ce bloc fait office de base de données interne qui va réserver de l’espace mémoire pour accueillir la trame d'octets envoyée par le script Python via Snap7.

Au sein de ce DB, chaque variable possède une adresse précise (un Offset) et un type :

- Des variables de type INT (Entiers 16 bits) pour stocker les valeurs absolues des coordonnées spatiales (X, Y) et de l'orientation (Angle).
- Des variables de type BOOL (Booléens / Bits) pour stocker les polarités de chaque coordonnée.
- Des bits d'état et de synchronisation pour valider que les données écrites par Python sont prêtes (Data Ready).
  
**2. Programme en langage LADDER**

La gestion du cycle et le transfert des données sont programmés en langage Ladder, structuré dans des blocs d'organisation ou de fonctions (OB/FC). Le programme se découpe en trois réseaux principaux :

-	Réseau 1 : Séquencement et lancement de l'exécution

<img width="800" height="177" alt="image" src="https://github.com/user-attachments/assets/b4aa3531-a735-451b-b7d8-319c217ec39d" />

Le programme Ladder surveille l'état du capteur de la cellule. Lorsqu'un contenant coupe le faisceau du capteur de présence sur le convoyeur, le programme passe un bit de synchronisation à 1 (Trigger Vision). Ce bit sert de point de départ automatique pour le script Python et la caméra Basler.

- Réseau 2 : Transfert des coordonnées vers la mémoire du robot

<img width="945" height="205" alt="image" src="https://github.com/user-attachments/assets/d7c2047d-8f28-4610-a3d5-0c414e51cda4" />

Une fois que le script Python a écrit les nouvelles coordonnées dans le DB, le programme Ladder entre dans une phase de transfert. Il récupère les valeurs numériques (X, Y, Angle). L'automate envoi ensuite ces données directement dans la mémoire du contrôleur du robot FANUC en utilisant une connexion profibus.

- Réseau 3 : Transfert des bits de polarité

 <img width="672" height="385" alt="image" src="https://github.com/user-attachments/assets/afe556c7-0c2b-4c56-989a-940ee8da068d" />

Simultanément au transfert des coordonnées numériques, le programme Ladder traite les bits de polarité stockés dans le DB. L'automate les envoie dans la mémoire du robot en utilisant des entrées numériques dédiées (Digital Inputs) via le réseau Profibus.


### Programme Robot (FANUC M10ia)

  <img width="385" height="626" alt="image" src="https://github.com/user-attachments/assets/e3cdfdcd-d3b1-4482-897d-3e651e8f981c" />

Une fois que l'automate a transmis les données sur le réseau Profibus, le contrôleur du robot prend le relais. Son rôle est de lire ces signaux bruts, de reconstruire la position réelle du colis, puis d'exécuter la trajectoire de saisie.

**1. Lecture et décodage des signaux (GI et DI)**
   
Le programme interne du robot vérifie en continu ses entrées pour acquérir la pose de la pièce :

- Les valeurs absolues sur les "Group Inputs" (GI) : Le robot lit les valeurs numériques de X, Y et l'Angle via des groupements d'entrées logiques codés sur 12 bits. Ce format d'entrées groupées permet de reconstruire les coordonnées en combinant l'état des 12 lignes physiques du bus.
- Le signe sur les "Digital Inputs" (DI) : En parallèle, le robot interroge des entrées digitales simples pour connaître la polarité de chaque coordonnée. Par exemple, si la DI[1] (dédiée à l'axe X) est à 1, le robot sait que la valeur lue sur le GI associé doit être interprétée comme un nombre négatif.
  
**2. Reconstitution et mise à l'échelle**

Les données reçues par le contrôleur sont des entiers bruts qui ont été multipliés par le programme python pour éviter les virgules. Le programme du robot applique donc un traitement de mise à l'échelle :

- Restauration de la décimale : Le robot divise par 10 les coordonnées lues sur les GI afin de retrouver la valeur réelle en millimètres (ou en degrés pour l'angle), restituant ainsi la précision d'un chiffre après la virgule.
- Calcul de la position finale : Le script applique le signe (polarité) et injecte ces composantes (X, Y, Angle) dans un registre de position.
  
**3. Saisie dynamique des colis**

Une fois le registre de position actualisé et le signal d'autorisation de l'automate reçu, le robot lance l’exécution du déplacement. Au lieu de descendre sur une trajectoire fixe, il applique le décalage calculé à sa trajectoire. Le bras articulé ajuste l'approche de sa pince en translation (X, Y) et pivote sur l’axe R3 (Angle) pour s'aligner parfaitement avec le colis. Le robot peut ensuite saisir le colis en conséquence, garantissant une prise fiable quelle que soit la position de la pièce sur le convoyeur.
 

