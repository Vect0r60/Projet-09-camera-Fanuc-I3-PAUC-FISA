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

Nous avons aussi pu validé la communication descendante. Les coordonnées calculées par Python sont transmises vers l'automate, qui les réceptionne et les stocke dans le bloc de données (DB) interne, ce qui doit permettre de les envoyer au robot par la suite.

# Difficultés techniques et solutions

## Communication avec le contrôleur FANUC


<img width="119" height="227" alt="image" src="https://github.com/user-attachments/assets/8c74df1a-83e7-48cb-95cf-0ddd10e78e27" />

La dernière phase d'essais ne s'est pas montrée concluante. En effet, la réception des données sur le contrôleur FANUC n'a pas pu être finalisée. Par conséquent, la reconversion des coordonnées ainsi que le repositionnement dynamique du robot n'ont pas pu être validés.

Cela s'explique par le fait que la structure initiale du bloc de données — configurée en 8 bits d'entrée et 10 bits de sortie — a dû être modifiée en raison d'une contrainte technique liée à l'architecture mémoire du contrôleur FANUC. Ce dernier ne disposait pas d'une gestion de mémoire optimisée pour traiter des données asymétriques ou de tailles non standardisées. Afin de garantir la compatibilité et d'éviter les erreurs de communication, la table d'échange a été harmonisée sur un format standard de 16 bits en entrée et 16 bits en sortie. Malgré cette reconfiguration, la liaison n'a pas pu être établie, et le manque de temps a fait de cette étape un point bloquant pour la finalisation du projet.

