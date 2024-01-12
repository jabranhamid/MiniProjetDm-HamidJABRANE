# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:12:29 2023

@author: Hamid Jabrane
"""
import pandas as pd
import streamlit as st
from openpyxl import load_workbook
import cv2
import matplotlib.pyplot as plt

import numpy as np

import os

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Affichage de l'image logo de FSTE et MASTER SIDI 
image_path = "enteteLogoIA.jpg"
st.image(image_path, use_column_width=True)
# le titre et le sujet de l'application Mini Projet
st.sidebar.write("<h2>MINI PROJET <font color='#01F5FA'>IA</font> </h2>", unsafe_allow_html=True)

st.sidebar.markdown(
             
    "<h3 style='color: blue;'>Encadré par: Pr. Imad ZEROUAL</h3>"
    "<h3 style='color: #040290;'>Réalisé par : Hamid JABRANE</h3> "
        "<h3>     </h3> " 
        
        "<h1></h1>"
        "<h4> Entrainer le modèle </h4>"
        "<h4>Tester le modèle</h4>"
        "<h4>Faire la prédiction</h4>"
    , unsafe_allow_html=True
    
    )


def import_excel():
    st.title("Importer un fichier Excel avec Streamlit")

    # Ajouter un bouton pour permettre à l'utilisateur de télécharger le fichier Excel
    uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx", "xls"])

    # Vérifier si un fichier a été téléchargé
    if uploaded_file is not None:
        return pd.read_excel(uploaded_file)
    else:
        return None

def afficher_donnees(df):
    st.subheader("Les premières données du fichier Excel:")
    st.dataframe(df.head())

def afficher_taille(df):
    st.subheader("Taille du fichier:")
    st.write(f"Nombre de lignes: {df.shape[0]}")
    st.write(f"Nombre de colonnes: {df.shape[1]}")

def afficher_info_excel(fichier_excel):
    st.subheader(f"Informations sur le nouveau fichier Excel '{fichier_excel}' :")

    # Charger le fichier Excel
    #df_excel = pd.read_excel(fichier_excel)

    # Afficher les premières lignes
    st.write("Aperçu des premières lignes du fichier Excel :")
    st.dataframe(fichier_excel.head())

    # Afficher la taille du fichier Excel
    st.write(f"Nombre total de lignes : {fichier_excel.shape[0]}")
    st.write(f"Nombre total de colonnes : {fichier_excel.shape[1]}")

    # Afficher les noms des colonnes
    st.write("Noms des colonnes :")
    st.write(list(fichier_excel.columns))



def main():
    # Importer le fichier Excel
    df = import_excel()

    # Vérifier si un fichier a été importé
    if df is not None:
        # Afficher les données et la taille du fichier
        afficher_donnees(df)
        afficher_taille(df)
        afficher_info_excel(df)
        # Utilisez cette fonction en passant le chemin de votre fichier Excel
         # Diviser les données en features (X) et target (y)
        X = df[['Age', 'Indicateur_Sociale', 'Test_Depression']]
        y = df['DegreDepression']

    # Diviser les données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer le modèle SVM
        model = SVC(kernel='linear', C=1.0, random_state=42)

# Entraîner le modèle sur l'ensemble d'entraînement
        model.fit(X_train, y_train)

# Définir une fonction pour faire des prédictions
        def faire_predictions(age, indicateur_sociale, test_estime_de_soi):
            new_data = pd.DataFrame({
                'Age': [age],
                'Indicateur_Sociale': [indicateur_sociale],
                'Test_Depression': [test_estime_de_soi]
                })
            predictions = model.predict(new_data)
            return predictions[0]

    # Interface utilisateur Streamlit
        st.title("Prédiction Degré de dépression")

# Ajouter des champs pour saisir les valeurs
        age = st.slider("Age:", min_value=0, max_value=100, step=1)
        indicateur_sociale = st.slider("Indicateur Sociale:", min_value=0, max_value=100, step=1)
        test_estime_de_soi = st.slider("Test Depression:", min_value=0, max_value=100, step=1)

# Faire des prédictions lorsque l'utilisateur clique sur un bouton
        if st.button("Faire des prédictions"):
            prediction = faire_predictions(age, indicateur_sociale, test_estime_de_soi)
            st.success(f"Prédiction Degré Dépression: {prediction}")
if __name__ == "__main__":
    main()
