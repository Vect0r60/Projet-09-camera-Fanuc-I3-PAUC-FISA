---
layout: default
nav_order: 7
title: Validations & Analyse critque
---

# Validations & Analyse critque

## 1. Montage physique et matériel

**Accomplissements :**

Le support de la caméra Basler et le boîtier de protection de la Raspberry Pi 5 ont été entièrement modélisés sur le logiciel Onshape et imprimés en 3D au sein du Markerspace de l'école.

- Montage du support : L'installation sur les profilés aluminium de la cellule de contionnement est robuste et stable. Elle intègre la caméra, son dissipateur thermique ainsi que le Raspberry Pi. La hauteur de fixation offre un champ de vision optimal, garantissant une acquisition d'image de qualité.

<img width="310" height="220" alt="image" src="https://github.com/user-attachments/assets/a2769a2c-dfd5-40ce-a3bf-9e30791ccddb" />

- Respect du Budget : L'intégralité de la solution matérielle a été conçue en exploitant les ressources existantes de l'école, ce qui permet d'afficher un coût total de 0 €.
  
**Axes d’améliorations :**

À ce stade, le câblage définitif (les câbles réseau et d'alimentation) n'est pas finalisé. Pour atteindre un standard industriel, ces liaisons doivent être intégrées proprement dans des goulottes afin d'éviter tout risque de déconnexion lors des mouvements de la cellule et de conflits avec les autres câbles déjà existants.

## 2. Fonctionnement et résultat logiciel
Algorithme performant et stable : Le script Python développé avec la bibliothèque OpenCV remplit parfaitement son rôle. Il applique des filtres de traitement d'image efficaces (seuillage, détection de contours) permettant d'isoler la boîte de son environnement (le convoyeur) sans faux positifs, quelles que soient les conditions de luminosité du laboratoire.


A faire gauthier succès et limites partie programmation
Les points bloquants : 
Complexité exponentielle de la partie logicielle : La mise en place de la chaîne de communication multi-protocoles et multi-matériels (Script Python avec OpenCV -> Automate en Ladder via Snap7 -> Robot Fanuc via entrées numériques) a représenté une complexité algorithmique et structurelle importante. Cette superposition de couches logicielles augmente également le risque de problèmes et d’erreurs et rend donc la maintenance ou le diagnostic plus difficile. 
Perte de précision potentielle lors de la conversion : La méthode de conversion actuelle implique de transformer les coordonnées réelles en nombres entiers (multipliés par 10) pour les transiter via des groupements d'entrées numériques (GI 12 bits) sur le robot, qui doit ensuite les diviser à nouveau. Ce processus de troncature et de reformatage des variables peut occasionner une légère perte de précision géométrique ou des limitations sur la plage opérationnelle des mouvements.
Sensibilité de l'analyse d'image : Le script Python s'appuie sur le filtrage des nuances de gris (bibliothèque OpenCV) pour localiser le colis et déterminer son angle. Cette approche par seuillage est particulièrement sensible aux variations de la luminosité ambiante du laboratoire PAUC, ce qui peut fausser la détection si l'éclairage de la pièce change.

## 3.	Répartition du temps

Le projet a souffert d'un déséquilibre classique en ingénierie : une sous-estimation du temps nécessaire au débogage informatique au profit du temps passé sur l'installation physique et la modélisation des pièces.
Voici la répartition approximative du temps : 
 
En résumé, cette répartition du temps met en lumière le principal défi de notre projet : nous avons maîtrisé la conception mécanique (CAO) et le développement des briques logicielles individuelles, mais nous avons sous-estimé le temps nécessaire à l'intégration finale. Ce déséquilibre a créé un goulot d'étranglement en fin de projet, confirmant une règle clé de l'ingénierie : dans un système multi-constructeurs (Siemens, Fanuc, Basler), le débogage de l'interopérabilité et de la communication est souvent la phase la plus complexe et la plus chronophage.
Conclusion Générale
Ce projet de fin d'études a été particulièrement formateur. Il nous a confrontés aux réalités concrètes de l'ingénierie de terrain : la théorie des systèmes communicants se heurte souvent à l'opacité des protocoles constructeurs (ici, la communication spécifique avec le contrôleur FANUC). Si la cellule n'est pas encore totalement opérationnelle pour une production en boucle fermée, la structure globale (mécanique, vision industrielle) est solidement implantée et validée. Le verrou technologique a été identifié et cartographié.
Au-delà de l'aspect purement technique, ce projet a été une expérience extrêmement motivante pour l'ensemble de l'équipe. Nous avons particulièrement apprécié évoluer au sein du laboratoire PAUC, qui offre un environnement technologique et industriel concret. Travailler sur du matériel de standard d'usine (automates Siemens, robots FANUC, caméras Basler) nous a permis de retrouver les exigences, les configurations et les problématiques terrain que nous côtoyons au quotidien dans nos entreprises respectives. Cette synergie entre notre formation à UniLaSalle et notre expérience professionnelle a renforcé notre autonomie et notre rigueur dans la gestion d'un projet d'intégration complexe.

