import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="DataCollect INF232", layout="wide")

st.title("📊 Application de Collecte : Mobilité Urbaine")
st.write("Projet de collecte de données pour le cours INF232.")

# --- INITIALISATION DE LA BASE DE DONNÉES (Simulation avec Session State) ---
if 'db_collecte' not in st.session_state:
    st.session_state.db_collecte = pd.DataFrame(columns=['Date', 'Transport', 'Distance_KM', 'Temps_Min'])

# --- SECTION 1 : COLLECTE DES DONNÉES ---
st.sidebar.header("📥 Formulaire de Saisie")
with st.sidebar.form("form_collecte"):
    transport = st.selectbox("Moyen de transport", ["Bus", "Taxi", "Marche", "Moto", "Voiture"])
    distance = st.number_input("Distance parcourue (en KM)", min_value=0.1, step=0.5)
    temps = st.number_input("Temps mis (en minutes)", min_value=1, step=1)
    
    submit = st.form_submit_button("Enregistrer la donnée")

if submit:
    nouvelle_donnee = {
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'Transport': transport,
        'Distance_KM': distance,
        'Temps_Min': temps
    }
    # Ajout à notre tableau de données
    st.session_state.db_collecte = pd.concat([st.session_state.db_collecte, pd.DataFrame([nouvelle_donnee])], ignore_index=True)
    st.success("Donnée enregistrée avec succès !")

# --- SECTION 2 : ANALYSE DESCRIPTIVE ---
col1, col2 = st.columns(2)

df = st.session_state.db_collecte

if not df.empty:
    with col1:
        st.subheader("📋 Données collectées")
        st.dataframe(df, use_container_width=True)
        
        # Statistique simple (Efficacité)
        st.metric("Total KM collectés", f"{round(df['Distance_KM'].sum(), 2)} km")

    with col2:
        st.subheader("📈 Analyse Visuelle")
        # Diagramme circulaire pour la répartition (Créativité)
        fig = px.pie(df, names='Transport', title="Répartition des modes de transport")
        st.plotly_chart(fig, use_container_width=True)
        
        # Graphique de performance
        fig2 = px.bar(df, x='Transport', y='Distance_KM', color='Transport', title="Distance totale par transport")
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("Le tableau de bord est vide. Utilisez le formulaire à gauche pour ajouter des données.")