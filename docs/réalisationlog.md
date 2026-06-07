---
layout: default
nav_order: 5
parent: Réalisations
title: Réalisations logicielle
---

# Réalisations logicielle

Pour valider le comportement du système de vision et sa communication, une série d'essais a été réalisée dans la cellule et sur l'automate :

<img width="718" height="956" alt="image" src="https://github.com/user-attachments/assets/0a26b158-fc99-4072-b84c-c5e2f555ce24" />

Les premiers tests ont confirmé la communication avec la caméra Basler. Le script Python assure la récupération continue du flux vidéo en direct, rendant les images disponibles pour la phase de traitement.

La réception du signal provenant du capteur de présence de la cellule a été validée. Dès que l'automate détecte un contenant, il transmet une instruction au script Python, ce qui déclenche la capture de l'image à analyser.

L'algorithme OpenCV traite l'image capturée. Le script isole le contenant, détermine ses coordonnées géométriques (X, Y) ainsi que son angle d'orientation, et les affiche sur le retour vidéo afin de permettre une vérification des valeurs en direct.

La dernière phase d'essais a validé la communication descendante. Les coordonnées calculées par Python sont transmises vers l'automate, qui les réceptionne et les stocke dans le bloc de données (DB) interne.

