# students-performance-system
C'est un dépôt qui contient l'analyse des données sur les performances des jeunes étudiants (15-18 ans) du niveau sécondaire ou lycée dependamment du système académique et la création d'un modèle de prédiction des performances académiques.

 Ce projet explore les divers facteurs qui influencent le succès scolaire, en se concentrant sur des éléments clés tels que :

    - **Niveau d'éducation des parents** : Comment le parcours éducatif des parents peut influencer les performances des étudiants.
    - **Aide des parents** : L'impact du soutien parental sur les résultats académiques.
    - **Temps d'études par semaine** : La relation entre le temps consacré aux études et les performances scolaires.
    - **Nombre d'absences par année** : Comment l'assiduité en classe se reflète sur les résultats scolaires.
    - **Mentorat** : L'influence du mentorat sur la performance académique des étudiants. Etc...
    Grâce à une analyse approfondie de ces critères, j'ai développé un modèle de prédiction qui permet d'anticiper les performances académiques des étudiants. 
    Ce modèle peut être utilisé pour identifier les points forts et les domaines d'amélioration, offrant ainsi des pistes pour soutenir et améliorer le parcours scolaire des jeunes.
    Cela montre également comment l'implication des parents dans l'apprentissage des jeunes peut les aider à accroitre leur niveau académique.

Explorez les différentes sections de l'application pour découvrir mes analyses exploratoires et prédictions personnalisées à l'adresse suivante : https://students-performance-system.streamlit.app/.

---
### Apropos des données utilisées
L'ensemble de données utilisé contient des informations complètes sur 2 392 élèves du secondaire  ou du lycée dépendamment du système académique (high school).
Il détaille les caractéristiques démographiques des étudiants (comme l'âge, le sexe, l'ethnie, ...), leurs habitudes d'étude (temps d'apprentissage par semaine, nombre d'absences, ...), 
l'implication des parents , les activités parascolaires (sports, bénévolat, musique, ...) et les résultats scolaires (note moyenne cumulative comprise entre 2.00 à 4.00). 
La moyenne cumulative est influencée par les différentes caractéristiques enumérées ci-dessus. La variable cible, GradeClass, classe les notes des élèves en catégories distinctes selon la
moyenne cumulative. Voici les différentes classes : **A : Excellent, B : Très bien, C : Bien, D : Passable et F : Echec**.

La source complète des données est disponible ici: https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset.
