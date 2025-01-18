import os
import streamlit as st

def app():
    st.write("Carte des immatriculations")
    
    base_path = os.path.abspath(os.path.dirname(__file__))
    html_path = os.path.join(base_path, '../../script/map/cartes/heatmap_population.html')
    with open(html_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    st.components.v1.html(html_content, height=600)