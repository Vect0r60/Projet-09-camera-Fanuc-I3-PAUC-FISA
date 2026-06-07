---
layout: default
nav_order: 5
parent: Réalisations
title: Réalisations logicielle
---

# Réalisations logicielle

Pour valider le comportement du système de vision et sa communication, une série d'essais progressifs a été réalisée sur la cellule :

Les premiers tests ont permis de confirmer la bonne communication avec la caméra Basler. Le script Python récupère avec succès le flux vidéo en direct, sans latence ni perte de frame, garantissant la disponibilité des images pour le traitement.

Nous avons validé la réception du signal provenant du capteur de présence de la cellule. Dès que l'automate détecte un contenant, il transmet un ordre au script Python, déclenchant instantanément la capture d'écran de l'image à analyser.

Lors des essais en condition, l'algorithme OpenCV a correctement traité l'image capturée. Le script parvient à isoler le contenant et à déterminer ses coordonnées géométriques (X, Y) ainsi que son angle d'orientation.

La dernière phase d'essais a validé la communication descendante. Les coordonnées calculées par Python sont envoyées avec succès vers l'automate, qui les réceptionne et les stocke dans sa base de données (DB) interne.

