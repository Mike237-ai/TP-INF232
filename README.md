# TP-INF232
# 🌍 EcoTrack Pro - Collecte & Analyse de Données

> **Projet académique :** TP INF232  
> **Développeur :** TCHOFFO BENI MIKEL  
> **Matricule :** 24G2339  
> **Filière :** Informatique

---

## 🚀 Présentation du Projet
**EcoTrack Pro** est une application web interactive conçue pour la collecte, le stockage et l'analyse descriptive des données de mobilité urbaine. L'objectif est de permettre aux utilisateurs de suivre leur empreinte carbone en temps réel tout en fournissant des outils d'analyse statistique avancés.

🔗 **Lien de l'application en ligne :** [https://tp-inf232-tchoffo-beni-mikel-24g2339.streamlit.app/](https://tp-inf232-tchoffo-beni-mikel-24g2339.streamlit.app/)

---

## ✨ Qualités de l'Application

### 🛠️ Robustesse
- **Validation des données :** Utilisation de formulaires typés (Streamlit Forms) pour empêcher la saisie de données erronées ou négatives.
- **Gestion d'état :** Utilisation de `session_state` pour assurer la persistance des données durant la session utilisateur.
- **Pipeline CI/CD :** Déploiement automatisé via GitHub Actions (fichier `.yml`) pour garantir l'intégrité du code.

### ⚡ Efficacité
- **Traitement temps réel :** Les calculs statistiques (Moyennes, totaux de CO2) se mettent à jour instantanément après chaque saisie.
- **Exportation rapide :** Fonction intégrée d'exportation de la base de données au format CSV pour une exploitation externe.
- **Performance :** Optimisation du chargement des graphiques grâce à l'utilisation de bibliothèques légères et performantes (Pandas & Plotly).

### 💡 Créativité (Secteur : Mobilité Durable)
- **Modélisation écologique :** Transformation automatique des distances parcourues en émissions de $CO_2$ selon le mode de transport.
- **UX/UI Interactive :** Design moderne avec menus de navigation, indicateurs visuels (KPI) et graphiques dynamiques (Sunburst, Area charts).

---

## 🛠️ Stack Technique
* **Langage :** Python 3.9+
* **Framework Web :** Streamlit
* **Analyse de données :** Pandas
* **Visualisation :** Plotly Express
* **Déploiement :** Streamlit Community Cloud

---

## 📂 Structure du Dépôt
* `app.py` : Code source principal de l'application.
* `requirements.txt` : Liste des dépendances Python nécessaires.
* `.github/workflows/deploy.yml` : Configuration de l'automatisation du déploiement.
* `README.md` : Documentation du projet.

---

## ⚙️ Installation Locale
Pour tester l'application sur votre machine :

1. Cloner le dépôt :
   ```bash
   git clone [https://github.com/ton-username/ton-repo.git](https://github.com/ton-username/ton-repo.git)

 2.  Installer les dépendances :
     pip install -r requirements.txt

 3. Lancer l'application :
    streamlit run app.py
