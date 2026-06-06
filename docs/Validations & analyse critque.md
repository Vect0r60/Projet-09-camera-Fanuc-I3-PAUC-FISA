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

**Accomplissements :**

La partie logicielle du projet est partiellement fonctionnelle et s'articule autour de trois accomplissements majeurs :

- Retour vidéo : Le script Python parvient à récupérer avec succès le retour vidéo en direct de la caméra Basler. Les images sont capturées en temps réel pour être directement exploitées par l'algorithme.
  
-	Récupération des coordonnées : Grâce à la bibliothèque OpenCV, le script traite l'image pour détecter le contenant, filtrer le bruit visuel et isoler avec précision ses coordonnées spatiales X, Y ainsi que son angle d'orientation.
  
- Communication avec l’automate : La communication avec l'automate fonctionne. Le script Python transmet bien les données de position calculées et gère l'échange de signaux au programme Ladder. Il est aussi capable de récupérer la valeur de détection du capteur de présence afin d’exécuter prise d’image.


## 3.	Répartition du temps

Le projet a souffert d'un déséquilibre classique en ingénierie : une sous-estimation du temps nécessaire au débogage informatique au profit du temps passé sur l'installation physique et la modélisation des pièces.
Voici la répartition approximative du temps : 
 
En résumé, cette répartition du temps met en lumière le principal défi de notre projet : nous avons maîtrisé la conception mécanique (CAO) et le développement des briques logicielles individuelles, mais nous avons sous-estimé le temps nécessaire à l'intégration finale. Ce déséquilibre a créé un goulot d'étranglement en fin de projet, confirmant une règle clé de l'ingénierie : dans un système multi-constructeurs (Siemens, Fanuc, Basler), le débogage de l'interopérabilité et de la communication est souvent la phase la plus complexe et la plus chronophage.
Conclusion Générale
Ce projet de fin d'études a été particulièrement formateur. Il nous a confrontés aux réalités concrètes de l'ingénierie de terrain : la théorie des systèmes communicants se heurte souvent à l'opacité des protocoles constructeurs (ici, la communication spécifique avec le contrôleur FANUC). Si la cellule n'est pas encore totalement opérationnelle pour une production en boucle fermée, la structure globale (mécanique, vision industrielle) est solidement implantée et validée. Le verrou technologique a été identifié et cartographié.
Au-delà de l'aspect purement technique, ce projet a été une expérience extrêmement motivante pour l'ensemble de l'équipe. Nous avons particulièrement apprécié évoluer au sein du laboratoire PAUC, qui offre un environnement technologique et industriel concret. Travailler sur du matériel de standard d'usine (automates Siemens, robots FANUC, caméras Basler) nous a permis de retrouver les exigences, les configurations et les problématiques terrain que nous côtoyons au quotidien dans nos entreprises respectives. Cette synergie entre notre formation à UniLaSalle et notre expérience professionnelle a renforcé notre autonomie et notre rigueur dans la gestion d'un projet d'intégration complexe.

