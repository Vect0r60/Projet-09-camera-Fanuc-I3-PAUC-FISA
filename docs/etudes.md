---
layout: default
nav_order: 3
title: Choix techniques
---

# Choix techniques 

## Placement technique 

Au cours de l'étude, plusieurs approches ont été envisagées pour intégrer la solution de vision au sein de la cellule de conditionnement. 

La première idée consistait à embarquer la caméra directement sur le bras du robot. Une autre alternative prévoyait de la suspendre à la grille supérieure de l'enceinte de sécurité. Néanmoins, ces configurations imposaient de lourdes contraintes techniques, notamment la nécessité de gérer la dynamique et les trajectoires du robot afin d'éviter tout risque de collision ou de détérioration du matériel de vision. 

Pour s'affranchir de ces contraintes, le choix s'est porté sur l'utilisation des profilés en aluminium de l'armature de la cellule comme structure porteuse. Cette solution offre une excellente rigidité, une grande liberté de positionnement et une sécurité totale vis-à-vis des mouvements du robot. Un profilé supplémentaire a été découpé et ajusté afin de suspendre la caméra parfaitement perpendiculaire au convoyeur. Cette structure accueille également l'unité de traitement, à savoir le Raspberry Pi 5. 

<p align="center">
<img width="442" height="252" alt="image" src="https://github.com/user-attachments/assets/8673b654-0c8c-46d7-a460-75303e2d2513" />
</p>

## Choix mécanique 

Conformément aux orientations définies précédemment, la structure porteuse a été réalisée à partir de profilés en aluminium. Ce choix modulaire garantit une grande flexibilité pour ajuster la position du support au sein de la cellule. 

La diversité des composants disponibles au laboratoire PAUC a permis de tester différentes sections de profilés. Les ressources technologiques du MakerSpace ont ensuite été exploitées pour découper les profilés aux cotes exactes requises par l'application. 

Pour assembler la structure, nous avons utilisé des inserts, des écrous et des boulons de différents diamètres. Notamment, des inserts M8 ont été privilégiés pour assurer la rigidité de la liaison entre les profilés. 

<p align="center">
<img width="882" height="222" alt="image" src="https://github.com/user-attachments/assets/95aef27d-a068-4117-b40c-7ea1700cf6c8" />
</p>

## Fonctionnement partie logicielle
 
Le cycle de fonctionnement s'amorce dès qu'un contenant en mouvement sur le convoyeur coupe le faisceau d'un capteur de présence. Cette détection est transmise au FANUC M10ia, qui relaie l'information à l'Automate (PLC1). Dès la réception de ce signal, l'automate génère un ordre de déclenchement automatique (trigger) à destination de notre script Python.

Le script Python lance ensuite l'exécution d'une capture d'image par la caméra Basler ACE. Une fois l’image récupérée, l'algorithme isole le contenant pour récupérer sa position exacte. Il calcule alors précisément ses coordonnées ainsi que son orientation sur le tapis (X, Y et Angle). Ces données sont transformées en coordonnées métriques et renvoyées vers l’automate.

Enfin, l’automate assure le stockage des données et envoie les variables de position converties vers la mémoire du robot FANUC. Ainsi, le robot n'exécute plus une trajectoire fixe et théorique, mais adapte la position et l'angle de sa pince à l'arrivée de chaque contenant.

<p align="center">
<img width="945" height="314" alt="image" src="https://github.com/user-attachments/assets/57281ed3-5011-4c9f-8dec-258e446b751c" />
</p>

