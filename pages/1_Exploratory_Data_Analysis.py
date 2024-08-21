# Création d'un dashboard pour l'analyse exploratoire des données
# Etape 1: Importation des librairies nécessaires
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px

# Etape 2: Chargement et préparation des données
# Chargement des données
@st.cache_data
def load_data():
    data = pd.read_csv("Datas/Students_performance_data_new.xls")

    return data

def update_value_and_fill_the_na_value(data):
    # Application de la fonction fillna directement sur les colonnes pour apporter des modifications
    # Utilisation d'un dictionnaire pour définir des valeurs des colonnes à modifier
    values = {"ParentalEducation": "No_Education", "ParentalSupport": "No_Support"}
    data = data.fillna(value=values)
    # Modification de Higer par Higher
    data["ParentalEducation"] = data["ParentalEducation"].str.replace("Higer", "Higher")

    return data

data = load_data()
data_cleaned = update_value_and_fill_the_na_value(data)

st.title("Analyse exploratoire des données")

# Suppression de la colonne StudentID
data = data_cleaned.drop("StudentID", axis=1)

# Affichage des premières lignes du dataset
st.write("Aperçu des données : ")
st.write(data.head())

# Création de deux colonnes (divise la page en 2 colonnes)
col1, col2 = st.columns(2)

# Sélection des attributs numériques et non numériques
numerical_attrs = data.select_dtypes(exclude="object")
string_attrs = data.select_dtypes(exclude=[np.int64, np.float64])

with col1:
    st.write("Nombre total d'enregistrements : ", len(data))
with col2:
    st.write("Nombre total d'attributs (variables) : ", len(data.columns), ". ",
             len(numerical_attrs.columns), " attributs numériques et ", 
             len(string_attrs.columns), " attributs catégoriels.")
    
# Créer une ligne séparatrice entre les sections
st.markdown("---")

st.markdown("### Visualisation des données")
# Etape 3: Création des widgets pour intéragir avec les données
# Sélection du type d'analyse
analysis_type = st.radio("Sélectionnez le type d'analyse :", ["Univariée", "Bivariée"])

### Analyse univariée
sns.set_style("darkgrid")
if analysis_type == "Univariée":
    st.write("**Analyse univariée**")
    
    # Sélection d'une colonne pour l'analyse univariée
    column = st.selectbox("Sélectionnez une colonne pour la visualisation univariée :", data.columns)
    
    # Vérification du type de la colonne
    if pd.api.types.is_numeric_dtype(data[column]):
        plt.figure(figsize=(8, 4))
        sns.histplot(data[column], kde=True, bins=20)
        plt.title(f"Distribution de {column}")
        plt.xlabel("Nombre")
        st.pyplot(plt)
        
    else:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=data[column], order=data[column].value_counts().index)
        plt.title(f"Répartition de {column}")
        plt.xlabel("Nombre")
        # Affichage du graphique avec Streamlit
        st.pyplot(plt)

### Analyse bivariée
elif analysis_type == "Bivariée":
    st.write("**Analyse bivariée**")
    
    # Sélection des colonnes pour l'analyse bivariée
    column1 = st.selectbox("Sélectionnez la première colonne :", data.columns)
    column2 = st.selectbox("Sélectionnez la seconde colonne :", data.columns)
    
    # Vérification si les deux colonnes sont numériques
    if ((data[column1].dtype in [np.int64, np.float64]) and 
        (data[column2].dtype in [np.int64, np.float64])):
        
        plt.figure(figsize=(8, 4))
        plt.title(f"Relation entre {column1} et {column2}")
        sns.scatterplot(data=data, x=column1, y=column2)
        # sns.regplot(data=data, x=column1, y=column2)
        st.pyplot(plt)
        
    else:
        # Sélection du type de graphique si les variables ne sont pas toutes numériques
        kind = st.selectbox("Sélectionnez le type de graphique pour les variables non numériques :", ["bar", "box", "violin"])
        plt.figure(figsize=(8, 4))
        sns.catplot(data=data, x=column1, y=column2, kind=kind)
        plt.title(f"Repartition des valeurs entre {column1} et {column2}")
        st.pyplot(plt)

# Etape 5: Ajout des indicateurs clés (KPIs)
st.markdown("---")
st.markdown("### Quelques statistiques")

# Création des colonnes pour afficher les dataframes cote à cote
col2, col3 = st.columns(2)

# Utilisation des colonnes
with col2:
    # Moyenne et ecart-type des notes des étudiants par Niveau d'éducation des parents.
    avg_and_std_by_parent_educ = data.groupby("ParentalEducation").agg({"GPA": ["mean", "std"]}).reset_index()
    st.write("Moyenne et ecart-type des notes selon le niveau d'éducation des parents")
    st.write(avg_and_std_by_parent_educ)

with col3:
    # Moyenne et ecart-type des notes des étudiants par Niveau d'aide des parents.
    avg_and_std_by_parent_supp = data.groupby("ParentalSupport").agg({"GPA": ["mean", "std"]}).reset_index()
    st.write("Moyenne et ecart-type des notes selon le niveau d'aide des parents")
    st.write(avg_and_std_by_parent_supp)

st.markdown("---")
col4, col5 = st.columns(2)

with col4:
    # Nombre d'étudiants par note et par age
    nb_students_by_grade_and_age = data.groupby(["GradeClass", "Age"])["GPA"].count().reset_index(name="Nombre")
    st.write("Nombre d'étudiants par note (grade) et par age")
    st.write(nb_students_by_grade_and_age)

with col5:
    # Nombre d'étudiants par note et par ethnie
    nb_students_by_grade_and_ethnicity = data.groupby(["GradeClass", "Ethnicity"])["GPA"].count().reset_index(name="Nombre")
    st.write("Nombre d'étudiants par note et par ethnie")
    st.write(nb_students_by_grade_and_ethnicity)