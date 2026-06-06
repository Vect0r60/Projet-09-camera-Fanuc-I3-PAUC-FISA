---
layout: default
nav_order: 3
title: Choix techniques
---

#Choix techniques 

##Placement technique 

Au cours de l'étude, plusieurs approches ont été envisagées pour intégrer la solution de vision au sein de la cellule de conditionnement. 

La première idée consistait à embarquer la caméra directement sur le bras du robot. Une autre alternative prévoyait de la suspendre à la grille supérieure de l'enceinte de sécurité. Néanmoins, ces configurations imposaient de lourdes contraintes techniques, notamment la nécessité de gérer la dynamique et les trajectoires du robot afin d'éviter tout risque de collision ou de détérioration du matériel de vision. 

Pour s'affranchir de ces contraintes, le choix s'est porté sur l'utilisation des profilés en aluminium de l'armature de la cellule comme structure porteuse. Cette solution offre une excellente rigidité, une grande liberté de positionnement et une sécurité totale vis-à-vis des mouvements du robot. Un profilé supplémentaire a été découpé et ajusté afin de suspendre la caméra parfaitement perpendiculaire au convoyeur (visée zénithale). Cette structure accueille également l'unité de traitement, à savoir le Raspberry Pi 5. 

  

 

##Choix mécanique 

Conformément aux orientations définies précédemment, la structure porteuse a été réalisée à partir de profilés en aluminium. Ce choix modulaire garantit une grande flexibilité pour ajuster la position du support au sein de la cellule. 

La diversité des composants disponibles au laboratoire PAUC a permis de tester différentes sections de profilés. Les ressources technologiques du MakerSpace ont ensuite été exploitées pour découper les profilés aux cotes exactes requises par l'application. 

Pour assembler la structure, nous avons utilisé des inserts, des écrous et des boulons de différents diamètres. Notamment, des inserts M8 ont été privilégiés pour assurer la rigidité de la liaison entre les profilés. 
