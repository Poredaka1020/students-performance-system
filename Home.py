import streamlit as st

st.set_page_config(
    page_title="Bienvenu(e)",
    page_icon="👋",
)

st.write("# Analyse et Prédiction de la Performance Académique des Étudiants ! 👋")

st.sidebar.success("Sélectionner une page au dessus")

st.markdown(
    """

    Bienvenue sur notre application dédiée à l'analyse et à la prédiction de la performance académique des étudiants âgés de 15 à 18 ans. 
    Ce projet explore les divers facteurs qui influencent le succès scolaire, en se concentrant sur des éléments clés tels que :

    - **Niveau d'éducation des parents** : Comment le parcours éducatif des parents peut influencer les performances des étudiants.
    - **Aide des parents** : L'impact du soutien parental sur les résultats académiques.
    - **Temps d'études par semaine** : La relation entre le temps consacré aux études et les performances scolaires.
    - **Nombre d'absences par année** : Comment l'assiduité en classe se reflète sur les résultats scolaires.
    - **Mentorat** : L'influence du mentorat sur la performance académique des étudiants. Etc...
    Grâce à une analyse approfondie de ces critères, j'ai développé un modèle de prédiction qui permet d'anticiper les performances académiques des étudiants. 
    Ce modèle peut être utilisé pour identifier les points forts et les domaines d'amélioration, offrant ainsi des pistes pour soutenir et améliorer le parcours scolaire des jeunes.
    Cela montre également comment l'implication des parents dans l'apprentissage des jeunes peut les aider à accroitre leur niveau académique.

    Explorez les différentes sections de l'application pour découvrir mes analyses exploratoires et prédictions personnalisées.

"""
)