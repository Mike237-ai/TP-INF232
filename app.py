import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="EcoSmart Analytics | INF232",
    page_icon="🌱",
    layout="wide"
)

# Style CSS pour rendre l'interface "Superbe"
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { border: 1px solid #4CAF50; padding: 10px; border-radius: 10px; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. TITRE ET ENTÊTE ---
st.title("📊 EcoSmart : Collecte & Analyse de Données")
st.markdown("### TP INF232 - Système de collecte robuste et interactif")

# --- 3. BASE DE DONNÉES TEMPORAIRE (Session State) ---
if 'db' not in st.session_state:
    # Quelques données initiales pour que l'app ne soit pas vide au départ
    st.session_state.db = pd.DataFrame([
        {'Date': '2026-04-22 08:00', 'Transport': 'Bus', 'Distance': 12.5, 'Temps': 45, 'CO2': 1.0},
        {'Date': '2026-04-22 09:30', 'Transport': 'Marche', 'Distance': 1.2, 'Temps': 15, 'CO2': 0.0}
    ])

# --- 4. BARRE LATÉRALE (COLLECTE) ---
st.sidebar.header("📥 Saisie des données")
with st.sidebar.form("form_saisie", clear_on_submit=True):
    mode = st.selectbox("Moyen de transport", ["Marche", "Vélo", "Moto", "Bus", "Voiture"])
    dist = st.number_input("Distance parcourue (km)", min_value=0.1, step=0.1)
    duree = st.number_input("Durée du trajet (min)", min_value=1, step=1)
    
    btn_valider = st.form_submit_button("Enregistrer la donnée")

# Logique de calcul (Créativité)
if btn_valider:
    # Facteurs d'émission fictifs (kg CO2 / km)
    facteurs = {"Marche": 0.0, "Vélo": 0.0, "Moto": 0.09, "Bus": 0.07, "Voiture": 0.18}
    co2_estime = round(dist * facteurs[mode], 2)
    
    nouvelle_ligne = {
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'Transport': mode,
        'Distance': dist,
        'Temps': duree,
        'CO2': co2_estime
    }
    st.session_state.db = pd.concat([st.session_state.db, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
    st.sidebar.success("Donnée ajoutée !")

# --- 5. DASHBOARD (ANALYSE DESCRIPTIVE) ---
df = st.session_state.db

# Ligne de statistiques clés (KPIs)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Trajets", len(df))
m2.metric("Distance Totale", f"{df['Distance'].sum()} km")
m3.metric("Émissions CO2", f"{df['CO2'].sum():.2f} kg")
m4.metric("Temps Moyen", f"{df['Temps'].mean():.1f} min")

st.divider()

# Onglets interactifs
tab_graph, tab_table = st.tabs(["📈 Visualisations", "📄 Données Brutes"])

with tab_graph:
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Répartition des transports")
        fig_pie = px.pie(df, names='Transport', hole=0.3, color_discrete_sequence=px.colors.sequential.Greens_r)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_right:
        st.subheader("Relation Distance / Temps")
        fig_scatter = px.scatter(df, x="Distance", y="Temps", color="Transport", size="CO2", hover_data=['Date'])
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab_table:
    st.subheader("Historique des collectes")
    st.dataframe(df, use_container_width=True)
    
    # Bouton de téléchargement (Efficacité)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Exporter en CSV", data=csv, file_name="donnees_collecte.csv", mime="text/csv")
