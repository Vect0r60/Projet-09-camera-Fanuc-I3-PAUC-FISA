---
layout: default
nav_order: 7
title: Validations & Analyse critque
---

# Validations & Analyse critque

## 1. Montage physique et matériel

**Accomplissements :**

Le support de la caméra Basler et le boîtier de protection de la Raspberry Pi 5 ont été entièrement modélisés sur le logiciel Onshape et imprimés en 3D au sein du Markerspace de l'école.

- L'installation sur les profilés aluminium de la cellule de contionnement est robuste et stable. Elle intègre la caméra, son dissipateur thermique ainsi que le Raspberry Pi. La hauteur de fixation offre un champ de vision optimal, garantissant une acquisition d'image de qualité.

<img width="310" height="220" alt="image" src="https://github.com/user-attachments/assets/a2769a2c-dfd5-40ce-a3bf-9e30791ccddb" />

- L'intégralité de la solution matérielle a été conçue en exploitant les ressources existantes de l'école, ce qui permet d'afficher un coût total de 0 €.
  
**Axes d’améliorations :**

À ce stade, le câblage définitif (les câbles réseau et d'alimentation) n'est pas finalisé. Pour atteindre un standard industriel, ces liaisons doivent être intégrées proprement dans des goulottes afin d'éviter tout risque de déconnexion lors des mouvements de la cellule et de conflits avec les autres câbles déjà existants.

## 2. Fonctionnement et résultat logiciel

**Accomplissements :**

La partie logicielle du projet est partiellement fonctionnelle et se concentre autour de trois accomplissements majeurs :

- Le script Python parvient à récupérer avec succès le retour vidéo en direct de la caméra Basler. Les images sont capturées en temps réel pour être directement exploitées par l'algorithme.

<img width="360" height="330" alt="image" src="https://github.com/user-attachments/assets/9d688945-bf43-4e4c-8c3b-dfe598e65807" />
  
-	Grâce à la bibliothèque OpenCV, le script traite l'image pour détecter le contenant, en filtrant et isolant avec précision ses coordonnées spatiales X, Y ainsi que son angle d'orientation.

  <img width="304" height="325" alt="image" src="https://github.com/user-attachments/assets/f5d08612-74ec-42b3-8675-06bc97ec5fdb" />
 
- La communication via snap7 avec l'automate fonctionne. Le script Python transmet bien les données de position calculées et gère l'échange de signaux au programme Ladder. Il est aussi capable de récupérer la valeur de détection du capteur de présence afin d’exécuter prise d’image.

**Axes d’améliorations :**

La dernière étape de la communication logicielle, à savoir la liaison directe avec le robot, n'est pas encore fonctionnelle. Pour atteindre l'objectif final de saisie dynamique, il reste à finaliser la réception et la conversion des données directement sur le contrôleur FANUC.

## 3.	Répartition du temps

Le déroulement du projet a mis en évidence un déséquilibre dans la gestion du calendrier, avec une part importante du temps consacrée à la conception mécanique et à l'installation physique, au détriment de la programmation et du débogage.

Voici la répartition approximative du temps par phase de développement :

 <img width="583" height="344" alt="image" src="https://github.com/user-attachments/assets/eb33ca73-f57e-4f97-a4db-28c60d397826" />

Ce graphique montre que si la modélisation CAO et l'assemblage physique du support sont finalisés, le temps nécessaire au développement logiciel a été sous-estimé. La programmation s'est avérée plus complexe que prévu, et ce manque d'anticipation dans le calendrier explique pourquoi la communication finale avec le robot n'a pas pu être finalisée.

# Conclusion Générale

Ce projet de fin d'études a été particulièrement formateur. Il nous a montré la réalité du terrain : en théorie, faire communiquer des machines semble simple. Même si la cellule n'est pas encore prête pour une production 100 % autonome avec l’intégration de notre projet, toute la base mécanique et le système de vision industrielle fonctionnent parfaitement. Le projet a des bases solides, et nous avons ciblé exactement les dernier problèmes techniques à résoudre.

Au-delà de l'aspect purement technique, ce projet a été une expérience extrêmement motivante pour l'ensemble de l'équipe. Nous avons particulièrement apprécié évoluer au sein du laboratoire PAUC, qui offre un environnement technologique et industriel concret. Travailler sur du matériel de standard d'usine (automates Siemens, robots FANUC, caméras Basler) nous a permis de retrouver les exigences, les configurations et les problématiques terrain que nous côtoyons au quotidien dans nos entreprises respectives. Cette synergie entre notre formation à UniLaSalle et notre expérience professionnelle a renforcé notre autonomie et notre rigueur dans la gestion d'un projet d'intégration complexe.


