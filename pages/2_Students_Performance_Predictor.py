import streamlit as st
import pandas as pd
import numpy as np
# import joblib
import pickle


# Chargement du modèle et le scaler
# scaler = joblib.load("scaler.pkl")
# model = joblib.load("best_model.pkl")

# Charger le modèle depuis le fichier
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as scale:
    scaler = pickle.load(scale)

st.title("Modèle de prédiction des performances académiques des étudiants de 15-18 ans.")

# Lire les données 
df_students = pd.read_csv("Datas/Students_performance_data_new.xls")

# df_students["Age"].unique()

# Renseigner les champs de saisie
st.write("Entrer les informations de l'étudiant pour faire une prédiction")

age = st.number_input("Âge (entre 15-18 ans)", min_value=15, max_value=18)
# gender = st.selectbox("Genre", df_students["Gender"].unique(), index=None,
#                       placeholder="Veuillez sélectionner...")
gender = st.selectbox("Genre", df_students["Gender"].unique())
ethnicity = st.selectbox("Ethnie", df_students["Ethnicity"].unique())
parental_education = st.selectbox("Niveau d'étudication des parents", ["No Education", "High School", "Some College", "Bachelor's", "Higher"])
study_time = st.number_input("Temps d'études par semaine en heure (entre 0-20)", min_value=0, max_value=20)
nb_absences = st.number_input("Nombre d'absences par année (0-30)", min_value=0, max_value=30)
tutoring = st.selectbox("Tutorat", df_students["Tutoring"].unique())
parental_support = st.selectbox("Support des parents", ["No Support", "Low", "Moderate", "High", "Very High"])
extracurricular = st.selectbox("Activités parascolaires", df_students["Extracurricular"].unique())
sports = st.selectbox("Sports", df_students["Sports"].unique())
music = st.selectbox("Musique", df_students["Music"].unique())
volunteering = st.selectbox("Bénévolat", df_students["Volunteering"].unique())
gpa = st.number_input("Note moyenne pondérée (0.0-4.0)", min_value=0.0, max_value=4.0)

if st.button("Prédire"):
    # Ecrire les conditions de vérification des entrées de l'utilisateur et l'encodage des données pour le machine learning
    # Pour le genre
    if gender == "Male":
        gender = 0
        # st.info(f"Le genre a été modifié en {gender}")
    else:
        gender = 1
        # st.info(f"Le genre a été modifié en {gender}")
    # else:
    #     st.error("Veuillez sélectionner un genre")
    
    # Pour l'ethnie
    if ethnicity == "Caucasian":
        ethnicity = 0
    elif ethnicity == "African_American":
        ethnicity = 1
    elif ethnicity == "Asian":
        ethnicity = 2
    else:
        ethnicity = 3
    
    # Pour le niveau d'éducation des parents
    if parental_education == "No Education":
        parental_education = 0
    elif parental_education == "High School":
        parental_education = 1
    elif parental_education == "Some College":
        parental_education = 2
    elif parental_education == "Bachelor's":
        parental_education = 3
    else:
        parental_education = 4

    # Pour tutorat
    if tutoring == "Yes":
        tutoring = 1
    else:
        tutoring = 0
    
    # Pour support des parents
    if parental_support == "No Support":
        parental_support = 0
    elif parental_support == "Low":
        parental_support = 1
    elif parental_support == "Moderate":
        parental_support = 2
    elif parental_support == "High":
        parental_support = 3
    else:
        parental_support = 4
    
    # Pour activités parascolaires
    if extracurricular == "Yes":
        extracurricular = 1
    else:
        extracurricular =0
    
    # Pour sports 
    if sports == "Yes":
        sports = 1
    else:
        sports = 0
    
    # Pour musique
    if music == "Yes":
        music = 1
    else:
        music = 0

    # Pour bénévolat 
    if volunteering == "Yes":
        volunteering = 1
    else:
        volunteering = 0
    
    # Création d'un tableau numpy 2D.
    datas = np.array([[age, gender, ethnicity, parental_education, study_time,
                      nb_absences, tutoring, parental_support, extracurricular,
                      sports, music, volunteering, gpa]])
    # st.write(datas)
    # Normaliser les données avec le scaler
    features_scaled = scaler.transform(datas)
    # st.write(features_scaled)

    # Application du modèle pour faire des prédictions
    prediction = model.predict(features_scaled)

    # Affichage de la prédiction
    # prediction[0] permet d'afficher uniquement la valeur sans les []
    # st.write(f"La prédiction est : {prediction[0]}")
    if prediction[0] == 0:
        message = "Vous semblez être un excellent élève, la note prédite est : **A (Excellent).**"
        st.info(message, icon="ℹ️")
    elif prediction[0] == 1:
        message = "Vous semblez être un très bon élève, la note prédite est : **B (Très bien).**"
        st.info(message, icon="ℹ️")
    elif prediction[0] == 2:
        message = "Vous semblez être un bon élève, la note prédite est : **C (Bien).**"
        st.info(message, icon="ℹ️")
    elif prediction[0] == 3:
        message = "Vous semblez être un élève moyen, la note prédite est : **D (Passable).**\n\
                Fournissez plus d'éfforts pour vous hisser vers le haut."
        st.warning(message, icon="⚠️")
    else:
        message = "Désolé, la note prédite est : **F (Echec).** Vous aurez tendance à travailler sur \n\
                 pas mal de point pour améliorer votre niveau comme : diminuer les absences, augmenter le nombre d'heures d'études par semaine,\n\
                 avoir peut-être l'aide de vos parents.\n\
                 Bon courage et bonne chance pour la suite."
        st.error(message, icon="❌")
    