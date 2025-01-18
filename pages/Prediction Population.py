import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy.optimize import curve_fit
import os 

# Définir le chemin absolu
base_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(base_path, '../data/cities_population.csv')
filtered_file_path = os.path.join(base_path, '../data/filtered_cities_population.csv')

if os.path.exists(file_path):
    # Charger les données
    df_pop = pd.read_csv(file_path, low_memory=False)
    
    df_pop = df_pop.loc[df_pop.groupby(['longitude', 'latitude', 'annee'])['valeur_population'].idxmax()]

    # Filtrer pour la France (contraintes de latitude et longitude)
    df_pop = df_pop[(df_pop['latitude'] >= 41.0) & (df_pop['latitude'] <= 51.5) & 
                    (df_pop['longitude'] >= -5.0) & (df_pop['longitude'] <= 9.5)]

    df_pop.to_csv(filtered_file_path, index=False)

    # Configuration de Streamlit pour afficher les résultats
    st.title("Estimation de la Population de 2011 à 2025")
    st.write("Voici une estimation de la population de la France métropolitaine pour les années à venir en utilisant différents modèles.")

    # Fonction pour calculer la population totale par année
    def somme_population_pour_annee(annee):
        res = df_pop[df_pop['annee'] == annee]['valeur_population'].sum()
        return res

    # Obtenir les années uniques et calculer la population pour chaque année
    # ...existing code...
else:
    st.error(f"Le fichier {file_path} est introuvable.")