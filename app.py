import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

# --- 1. CONFIGURATION AVANCÉE DE LA PAGE ---
st.set_page_config(page_title="EcoTrack Pro | INF232", page_icon="🌍", layout="wide")

# --- 2. CSS SUBLIME (Design de l'application) ---
st.markdown("""
    <style>
    /* Arrière-plan général et police */
    .stApp { background-color: #f8f9fa; }
    
    /* Style des cartes de statistiques (KPIs) */
    [data-testid="stMetricValue"] { color: #2e7d32; font-size: 30px !important; font-weight: bold; }
    [data-testid="stMetricLabel"] { color: #546e7a; font-size: 16px !important; }
    div[data-testid="metric-container"] {
        background-color: white; border-radius: 15px; padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 5px solid #2e7d32;
    }
    
    /* Boutons interactifs avec effet Hover */
    .stButton>button {
        background-image: linear-gradient(to right, #4CAF50 , #2E7D32);
        color: white; border-radius: 25px; border: none; padding: 10px 25px; transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(46, 125, 50, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BASE DE DONNÉES SIMULÉE (Mémoire de l'app) ---
if 'db' not in st.session_state:
    st.session_state.db = pd.DataFrame([
        {'Date': '2026-04-20 08:00', 'Transport': 'Bus', 'Distance': 12.0, 'Temps': 40, 'CO2': 0.84, 'Ville': 'Yaoundé'},
        {'Date': '2026-04-21 09:30', 'Transport': 'Marche', 'Distance': 2.5, 'Temps': 30, 'CO2': 0.0, 'Ville': 'Douala'},
        {'Date': '2026-04-22 07:45', 'Transport': 'Voiture', 'Distance': 8.0, 'Temps': 25, 'CO2': 1.44, 'Ville': 'Yaoundé'}
    ])

df = st.session_state.db

# --- 4. BARRE DE NAVIGATION LATERALE ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3004/3004128.png", width=100)
st.sidebar.title("🌍 EcoTrack Pro")
menu = st.sidebar.radio("Navigation Menu", ["📊 Tableau de Bord", "📥 Saisir un trajet", "📂 Gestion des Données"])
st.sidebar.divider()
st.sidebar.info("**Projet INF232**\n\nCréativité, Robustesse, Efficacité.")

# ==========================================
# PAGE 1 : TABLEAU DE BORD (Analyses Poussées)
# ==========================================
if menu == "📊 Tableau de Bord":
    st.title("📊 Vue d'ensemble des mobilités")
    st.markdown("Analysez vos habitudes et votre impact écologique en un clin d'œil.")
    
    # KPIs Animés
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Trajets", len(df), "Collecte active")
    col2.metric("Distance Cumulée", f"{df['Distance'].sum()} km", "+ de kilomètres")
    col3.metric("Empreinte CO2", f"{df['CO2'].sum():.2f} kg", "- réduire l'impact", delta_color="inverse")
    
    # Barre de progression d'objectif écologique
    st.markdown("### 🎯 Objectif Réduction CO2 Mensuel")
    progress = min(df['CO2'].sum() / 10, 1.0) # Simulation objectif 10kg
    st.progress(progress)
    
    st.divider()
    
    # Graphiques Sublimes avec Plotly
    c1, c2 = st.columns(2)
    with c1:
        # Graphique Sunburst (Très créatif et pro)
        st.subheader("Répartition par Ville et Transport")
        fig_sun = px.sunburst(df, path=['Ville', 'Transport'], values='Distance', 
                              color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig_sun, use_container_width=True)
        
    with c2:
        # Graphique en aires (Tendances)
        st.subheader("Évolution de l'empreinte carbone")
        fig_area = px.area(df, x="Date", y="CO2", color="Transport", markers=True,
                           color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_area, use_container_width=True)

# ==========================================
# PAGE 2 : FORMULAIRE DE COLLECTE (Robustesse)
# ==========================================
elif menu == "📥 Saisir un trajet":
    st.title("📥 Enregistrer une nouvelle mobilité")
    
    with st.container():
        st.markdown("Remplissez le formulaire ci-dessous. Les données sont validées automatiquement.")
        with st.form("form_saisie", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                ville = st.selectbox("📍 Ville", ["Yaoundé", "Douala", "Bafoussam", "Autre"])
                mode = st.selectbox("🚲 Mode de transport", ["Marche", "Vélo", "Moto", "Bus", "Voiture"])
            with col2:
                dist = st.number_input("📏 Distance (km)", min_value=0.1, max_value=1000.0, step=0.5)
                duree = st.slider("⏱️ Durée (minutes)", 1, 300, 15)
            
            submit = st.form_submit_button("🚀 Enregistrer dans le Cloud")

        if submit:
            with st.spinner("Analyse et sécurisation des données..."):
                time.sleep(1) # Simule un traitement complexe
                facteurs = {"Marche": 0.0, "Vélo": 0.0, "Moto": 0.09, "Bus": 0.07, "Voiture": 0.18}
                co2_calc = round(dist * facteurs[mode], 2)
                
                new_row = {'Date': datetime.now().strftime("%Y-%m-%d %H:%M"), 'Transport': mode, 'Distance': dist, 'Temps': duree, 'CO2': co2_calc, 'Ville': ville}
                st.session_state.db = pd.concat([st.session_state.db, pd.DataFrame([new_row])], ignore_index=True)
                
                st.balloons() # Animation de succès
                st.toast("✅ Donnée enregistrée avec succès !", icon="🎉")

# ==========================================
# PAGE 3 : GESTION DES DONNÉES (Efficacité)
# ==========================================
elif menu == "📂 Gestion des Données":
    st.title("📂 Base de données et Export")
    
    st.markdown("### 🔍 Filtrer les données")
    filtre_ville = st.multiselect("Par Ville", options=df['Ville'].unique(), default=df['Ville'].unique())
    df_filtre = df[df['Ville'].isin(filtre_ville)]
    
    # Affichage de la table avec design interactif
    st.dataframe(df_filtre, use_container_width=True, hide_index=True)
    
    st.divider()
    
    colA, colB = st.columns(2)
    with colA:
        # Bouton d'export sécurisé
        csv = df_filtre.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Exporter la base (CSV)", data=csv, file_name="ecotrack_data.csv", mime="text/csv")
    with colB:
        # Bouton de nettoyage (Reset)
        if st.button("🗑️ Vider la base de données"):
            st.session_state.db = pd.DataFrame(columns=['Date', 'Transport', 'Distance', 'Temps', 'CO2', 'Ville'])
            st.toast("Base de données réinitialisée.", icon="⚠️")
            time.sleep(1)
            st.rerun()
