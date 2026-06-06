---
layout: default
nav_order: 2
title: Objectifs du projet
---

# Contexte & Objectifs

## Contexte du projet

Dans le cadre de notre formation d'ingénieur au sein d'UniLaSalle Amiens, nous évoluons au cœur d'une Usine 4.0. Cette infrastructure moderne intègre notamment une cellule de conditionnement automatisée dédiée à la gestion d'impressions 3D.

Le flux opérationnel actuel repose sur un circuit de tapis roulant qui achemine les pièces issues de l'impression 3D. En bout de ligne, un bras robotisé articulé FANUC M-10iA intervient pour saisir ces éléments et assurer leur transfert vers un second robot, chargé quant à lui de la manutention et de la palettisation de la cargaison.

## Problématique et limites du système existant

Bien que la cellule automatisée soit fonctionnelle, le processus souffre actuellement de limites de performance critiques liées à l'absence de retour d'information sensoriel (système en boucle ouverte). Le robot FANUC M-10iA doit saisir une boîte en carton contenant les impressions, mais sa programmation actuelle repose sur des coordonnées fixes.
Or, la réalité physique du convoyage introduit deux incertitudes majeures :

- Variabilité de la position (Translation) : En raison des frottements et de la cinématique du tapis roulant, la position finale de la boîte en carton peut être légèrement déviée de sa trajectoire nominale.
- Variabilité de l'orientation (Rotation) : Selon la manière dont la boîte se dépose sur le tapis, son angle d'orientation varie. Cela pose un problème majeur car son ouverture supérieure n'est plus correctement alignée pour la réception de la cargaison.
	
Ces incertitudes génèrent des échecs lors du transfert entre les deux robots (collisions, mauvaise préhension, chutes de colis), ce qui pénalise donc le rendement global de l'Usine 4.0.

## Cahier des charges fonctionnel

L'objectif principal du projet est d'intégrer une solution de vision industrielle low-cost permettant de guider le robot FANUC en temps réel. Le système devra remplir les fonctions suivantes :

- Détecter la présence de la boîte en carton en bout de convoyeur.
- Calculer les coordonnées spatiales précises (X, Y) et l'angle de rotation (θ) de la boîte.
- Communiquer ces corrections de trajectoire au contrôleur du robot FANUC M-10iA.
- Garantir une répétabilité et une fiabilité de prise supérieure à 98%.
	
## Contraintes du projet

La réussite de l’intégration du système de vision industrielle repose sur le respect de plusieurs contraintes que nous avons identifié :

Contrainte Budgétaire : Bien que nous disposions initialement d’une enveloppe budgétaire prévisionnelle de 150 €, nous avons finalement utiliser 0 €. Cette contrainte financière nous a poussés à être ingénieux : nous avons optimisé l’utilisation des équipements industriels déjà présents dans nos laboratoires et nous nous sommes tournés vers la récupération (chutes de profilés, visserie disponible) pour concevoir notre solution sans aucun coût supplémentaire.

Contrainte Temporelle : Pour réaliser ce projet, nous avions 50 heures planifiées. En pratique, ce volume horaire est plutôt faible pour un projet de cette envergure. De plus, il est difficile, de travailler sur le projet en dehors de ces heures prévues. Notre rythme en alternance impose une coupure lors des périodes en entreprise, où notre charge de travail professionnelle est élévé. À l'inverse, lors de nos périodes à l'école, l'emploi du temps académique est déjà chargé. Enfin, la nature même de notre projet d’ingénierie imposait une contrainte majeure : nous avions un besoin critique d’être physiquement présents dans les laboratoires pour effectuer nos tests, câbler les modules et manipuler le robot FANUC.

## Infrastructures disponibles et inventaire du matériel 

Pour réaliser notre projet, nous avons pu nous appuyer sur l’infrastructure industrielle moderne du Laboratoire PAUC (Production Automatisée et Usine Connectée) ainsi que sur le Makerspace d'UniLaSalle : 
Infrastructure Makerspace : Ce pôle regroupe le parc d'imprimantes 3D qui génèrent les pièces et d’autres machines notamment 2 découpeuses laser, scie, fer à souder. 
Voici les imprimantes utilisées pour la réalisation de nos 4 pièces en PLA (acide polylactique) :

<img width="314" height="232" alt="image" src="https://github.com/user-attachments/assets/c0e3cbe8-f708-4ec6-a6c3-9c9ef5806273" frameborder="0"/>

Infrastructure Robotique : Notre laboratoire est équipé de deux robots industriels. Pour notre application, nous avons exploité le bras articulé FANUC M-10iA, qui fait office d'actionneur final pour la préhension et le déplacement des colis.

<img width="586" height="282" alt="image" src="https://github.com/user-attachments/assets/aeff5c99-1021-45b3-8520-2ff4b5aff900" />

Cellule de conditionnement       &      Robot FANUC M-10iA

L'intégration de la solution de vision industrielle au sein de l'Usine 4.0 repose sur un écosystème matériel hybride, articulé autour de quatre axes majeurs : le traitement de l'information, l'infrastructure réseau, la structure mécanique et la connectique.

Caméra POE : C’est la pièce maîtresse du système de vision, fournie directement parmi le matériel existant de la cellule. Elle est installée au-dessus du tapis roulant pour capturer les images de la boîte en haute résolution. Sa technologie POE (Power over Ethernet) est un grand avantage technique : elle permet de faire passer à la fois l'alimentation électrique et les données d'images dans un seul et unique câble réseau (RJ45), ce qui simplifie grandement l'installation.

<img width="203" height="182" alt="image" src="https://github.com/user-attachments/assets/4e8bb1ba-7fb9-4e71-b59d-a1456915ac44" />

Raspberry Pi 5 : Placée au cœur du système de vision, la Raspberry Pi 5 a été choisie pour sa puissance de calcul CPU/GPU accrue et sa gestion optimisée du multitâche. Elle fait office de calculateur embarqué : elle récupère le flux vidéo de la caméra via le réseau, exécute les scripts de traitement d'images (traitement de forme, calcul du centre de gravité et de l'orientation de la boîte) et transmet les coordonnées de correction (X, Y, θ) au contrôleur du robot.
 
<img width="195" height="145" alt="image" src="https://github.com/user-attachments/assets/5925d191-d7fd-41cd-bda2-2facb900f5da" />

Switch Ethernet TP-Link : Il fonctionne comme une « multiprise » dédiée aux données. Au lieu de distribuer du courant, il centralise et distribue les informations de la cellule. C’est le point de connexion unique qui relie la caméra, la Raspberry Pi 5 et le robot FANUC. Grâce à lui, tous ces appareils partagent le même réseau et peuvent communiquer entre eux sans aucune latence.
 
<img width="246" height="161" alt="image" src="https://github.com/user-attachments/assets/4e5ef571-c53c-49bd-81a9-2494587eb7fd" />

Câblage de la cellule : Pour assurer l'alimentation des équipements et le transit de nos données (notamment via le protocole Snap7 pour faire communiquer notre script Python avec l'Automate jusqu'aux entrées du robot FANUC), nous avons uniquement utilisé du câble Ethernet et d'autres types de câbles.
 

