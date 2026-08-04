import base64
from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).parent / "assets"


def _img_b64(filename: str) -> str:
    p = ASSETS / filename
    if p.exists():
        return base64.b64encode(p.read_bytes()).decode()
    return ""

st.set_page_config(
    page_title="Josy Elices-Diez · Data Analyst",
    layout="wide",
    initial_sidebar_state="expanded",
)

CSS = """
<style>
[data-testid="stSidebar"] { background: #1A1A2E; }
[data-testid="stSidebar"] p { color: #6B6B8A !important; }
[data-testid="stSidebar"] hr { border-color: #2E2E4E; }
.stTabs [data-testid="stTab"] {
    font-size: 0.95rem;
    font-weight: 600;
    color: #5A6A7A;
    padding: 0.6rem 1.5rem;
}
.stTabs [data-testid="stTab"][aria-selected="true"] {
    color: #1E6091;
    border-bottom: 3px solid #1E6091;
}
.sb-name {
    color: #FFFFFF !important;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 0.75rem 0 0.1rem 0;
    letter-spacing: -0.01em;
    text-align: center;
}
.sb-role {
    color: #7EB8D4 !important;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0 0 0.4rem 0;
    text-align: center;
}
.sb-label {
    color: #5A5A78 !important;
    font-size: 0.54rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 700;
    margin: 0 0 0.15rem 0;
}
.sb-value {
    color: #8A92A8 !important;
    font-size: 0.66rem;
    margin: 0 0 0.1rem 0;
}
.sb-photo-wrap {
    width: 145px;
    height: 145px;
    border-radius: 50%;
    overflow: hidden;
    margin: 0.75rem auto 0 auto;
    border: 2px solid #2E86C1;
    flex-shrink: 0;
}
.sb-photo {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 32%;
    transform: scale(1.6);
    transform-origin: center 38%;
    display: block;
}
section[data-testid="stMain"] { background: #F5F7FA; }

.hero-card {
    background: white;
    border-radius: 14px;
    padding: 2.5rem;
    box-shadow: 0 2px 24px rgba(0,0,0,0.07);
    margin-bottom: 1.5rem;
}
.hero-name {
    font-size: 3rem;
    font-weight: 800;
    color: #1E2D3D;
    margin: 0 0 0.2rem 0;
    letter-spacing: -0.02em;
}
.hero-title {
    font-size: 1.25rem;
    color: #1E6091;
    font-weight: 600;
    margin: 0 0 1rem 0;
}
.hero-bio {
    color: #4A5A6A;
    line-height: 1.75;
    margin-bottom: 1.25rem;
    font-size: 0.95rem;
}
.hero-double-profil {
    display: inline-block;
    background: #EBF4FF;
    border-left: 4px solid #1E6091;
    border-radius: 6px;
    padding: 0.55rem 1rem;
    font-size: 0.95rem;
    font-weight: 700;
    color: #1E2D3D;
    margin-bottom: 1.25rem;
}
.hero-double-profil span {
    color: #1E6091;
}
.hero-link {
    display: inline-block;
    color: #1E6091;
    font-size: 0.875rem;
    text-decoration: none;
    margin-right: 1.25rem;
    font-weight: 500;
}
.hero-link-cv {
    background: #1E6091;
    color: white !important;
    border-radius: 20px;
    padding: 0.3rem 1rem;
    font-weight: 600;
}
.info-card {
    background: white;
    border-radius: 14px;
    padding: 1.75rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.06);
    height: 100%;
}
.info-card h4 {
    color: #1E2D3D;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.75rem;
    font-weight: 700;
}
.info-card p { color: #5A6A7A; font-size: 0.875rem; margin: 0.25rem 0; }
.skill-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}
.skill-card h4 {
    color: #1E2D3D;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.75rem;
    font-weight: 700;
}
.skill-tags-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-top: 0.25rem;
}
.skill-tag {
    background: #EBF4FF;
    color: #1E6091;
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.72rem;
    font-weight: 500;
    white-space: nowrap;
}
.project-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    display: flex;
    flex-direction: column;
    height: 100%;
}
.project-img {
    width: 100%;
    height: 175px;
    object-fit: cover;
    display: block;
}
.project-body {
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    border-top: 3px solid #1E6091;
}
.project-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: #1E2D3D;
    margin: 0 0 0.5rem 0;
    line-height: 1.4;
}
.project-desc {
    font-size: 0.84rem;
    color: #5A6A7A;
    line-height: 1.6;
    margin-bottom: 1rem;
    flex-grow: 1;
}
.cat-badge {
    display: inline-block;
    background: #F0F7FF;
    color: #1E6091;
    border: 1px solid #BDD9F2;
    border-radius: 12px;
    padding: 0.15rem 0.6rem;
    font-size: 0.7rem;
    margin: 0.15rem;
    font-weight: 500;
}
.tools-line {
    font-size: 0.75rem;
    color: #8A9BAB;
    margin: 0.75rem 0 0.5rem 0;
}
.gh-link {
    font-size: 0.82rem;
    color: #1E6091;
    text-decoration: none;
    font-weight: 600;
}
.section-title {
    font-size: 1.75rem;
    font-weight: 800;
    color: #1E2D3D;
    margin-bottom: 0.25rem;
    letter-spacing: -0.01em;
}
.section-bar {
    height: 4px;
    width: 48px;
    background: #1E6091;
    border-radius: 2px;
    margin-bottom: 1.5rem;
}
</style>
"""

PROJECTS = [
    {
        "title": "Analyse des ventes — Identification des produits rentables",
        "description": "10+ requêtes SQL complexes (jointures, agrégats, sous-requêtes) pour identifier les vins et régions les plus rentables.",
        "categories": ["SQL", "Bases de données", "Analyse de données"],
        "tools": "SQL · SQLite · DBeaver",
        "url": "https://github.com/Elicesjo/PROJET-2-",
        "image": "projet_02.png",
    },
    {
        "title": "Sous-nutrition mondiale — Cartographie et causes structurelles",
        "description": "Analyser les données FAO pour cartographier la sous-nutrition mondiale et identifier ses causes structurelles.",
        "categories": ["Python", "Visualisation", "Analyse exploratoire"],
        "tools": "Python · Pandas · Matplotlib · Jupyter",
        "url": "https://github.com/Elicesjo/PROJET-3-",
        "image": "projet_03.png",
    },
    {
        "title": "Base de données immobilière — Modélisation 500K transactions",
        "description": "Concevoir et peupler une base SQL normalisée (3NF) à partir de 500 000 transactions DVF — schéma relationnel complet.",
        "categories": ["SQL", "Bases de données", "Modélisation"],
        "tools": "SQL · PostgreSQL · DBeaver · Excel",
        "url": "https://github.com/Elicesjo/PROJET-4-",
        "image": "projet_04.png",
    },
    {
        "title": "Audit qualité de données — E-commerce vins en ligne",
        "description": "Détecter et corriger les doublons, valeurs manquantes et incohérences dans les données d'une boutique de vins en ligne.",
        "categories": ["Python", "Nettoyage de données", "Pandas"],
        "tools": "Python · Pandas · Jupyter · Matplotlib",
        "url": "https://github.com/Elicesjo/PROJET-5-",
        "image": "projet_05.png",
    },
    {
        "title": "Dashboard RH — Suivi santé de 1 200 collaborateurs",
        "description": "Tableau de bord interactif (filtres dynamiques, drill-down, DAX) pour le suivi des KPIs santé de 1 200 collaborateurs.",
        "categories": ["Power BI", "Dashboard", "DAX"],
        "tools": "Power BI · DAX · Excel",
        "url": "https://github.com/Elicesjo/PROJET-6-",
        "image": "projet_06.png",
    },
    {
        "title": "Pipeline dbt — Apprenants vs. marché du travail national",
        "description": "Modéliser un pipeline dbt end-to-end pour comparer les profils des apprenants OpenClassrooms au marché du travail national.",
        "categories": ["Python", "SQL", "dbt", "Data Engineering"],
        "tools": "Python · dbt · SQL · Pandas · Quarto",
        "url": "https://github.com/Elicesjo/PROJET-7-",
        "image": "projet_07.png",
    },
    {
        "title": "Segmentation RFM — Profilage de 2 500 clients e-commerce",
        "description": "Segmenter 2 500 clients en profils RFM et tester statistiquement les différences de comportement d'achat.",
        "categories": ["Python", "Statistiques", "Visualisation"],
        "tools": "Python · Pandas · Matplotlib · Seaborn · SciPy · Jupyter",
        "url": "https://github.com/Elicesjo/PROJET-8-",
        "image": "projet_09.png",
    },
    {
        "title": "Accès à l'eau potable — Analyse géopolitique dans 180 pays",
        "description": "Analyser l'accès à l'eau potable et les facteurs de mortalité liés dans 180+ pays via un dashboard Tableau interactif.",
        "categories": ["Tableau", "Dashboard", "Python", "Analyse de données"],
        "tools": "Tableau · Python · Pandas · Jupyter",
        "url": "https://github.com/Elicesjo/PROJET-9-",
        "image": "projet_09_eau.png",
    },
    {
        "title": "Stratégie d'export — Ciblage de marchés internationaux",
        "description": "Identifier des groupements de pays cibles pour l'export de poulets bio via ACP et clustering (CAH + K-means).",
        "categories": ["Python", "ACP", "Clustering", "Analyse de données"],
        "tools": "Python · Pandas · Scikit-learn · Matplotlib · Seaborn · Jupyter",
        "url": "https://github.com/Elicesjo/PROJET-10-",
        "image": "projet_11.png",
    },
    {
        "title": "Détection de faux billets — Classification automatisée vrai/faux",
        "description": "Comparer 4 algorithmes (K-means, régression logistique, KNN, Random Forest) pour détecter les faux billets à partir de mesures physiques, avec script CLI de prédiction déployable en production.",
        "categories": ["Python", "Machine Learning", "Classification"],
        "tools": "Python · Pandas · Scikit-learn · Matplotlib · Seaborn · Jupyter",
        "url": "https://github.com/Elicesjo/PROJET-11-",
        "image": "projet_faux_billets.png",
    },
]

for _p in PROJECTS:
    _p["_b64"] = _img_b64(_p["image"])

SKILLS = {
    "Langages & outils": [
        "Python", "SQL", "dbt", "Power BI", "Tableau",
        "Excel", "Git", "Jupyter", "Quarto",
    ],
    "Bases de données & modélisation": [
        "PostgreSQL", "MySQL", "SQLite", "DBeaver", "pgAdmin",
        "Modélisation relationnelle", "Schéma en étoile", "ETL", "Data warehouse",
    ],
    "Méthodes analytiques": [
        "Segmentation RFM", "ACP", "Clustering", "Tests statistiques",
        "Analyse exploratoire", "Visualisation", "Régression",
        "Analyse de cohortes", "A/B testing",
    ],
    "Expertise métier — Retail": [
        "Pilotage KPIs", "Analyse des ventes", "Reporting opérationnel",
        "Management d'équipes", "Stratégie commerciale", "Gestion P&L",
        "Formation équipes", "Retail analytics", "Analyse marché",
    ],
    "AI & Automatisation": [
        "OpenAI API", "Prompt engineering", "Analytics automatisée",
        "Automatisation rapports", "LLM", "No-code AI",
    ],
    "Langues": ["Français — natif", "Anglais — C1", "Espagnol — A2"],
}

ALL_CATEGORIES = sorted({cat for p in PROJECTS for cat in p["categories"]})


def tags_html(items, css_class):
    return "".join(f'<span class="{css_class}">{i}</span>' for i in items)


def page_home():
    st.markdown("""
    <div class="hero-card">
        <p class="hero-name">Josy Elices-Diez</p>
        <p class="hero-title">Data Analyst · Analytics & Automatisation IA</p>
        <p class="hero-bio">
        Data Analyst formée à <strong>OpenClassrooms × ENSAE</strong>, avec 10 ans d'expérience opérationnelle
        en retail dont 5 en management multisites. Je traduis des données complexes en décisions business.
        </p>
        <p class="hero-double-profil">
        Double profil — <span>rigueur analytique</span> &amp; <span>lecture immédiate du contexte métier.</span>
        </p>
        <a class="hero-link" href="mailto:josy.elices@gmail.com">✉ josy.elices@gmail.com</a>
        <a class="hero-link" href="https://www.linkedin.com/in/josy-elices-diez-03523225a/" target="_blank">LinkedIn</a>
        <a class="hero-link" href="https://github.com/Elicesjo" target="_blank">GitHub</a>
        <a class="hero-link hero-link-cv" href="app/static/cv_josy.pdf" target="_blank">↓ CV</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Compétences</p><div class="section-bar"></div>', unsafe_allow_html=True)

    skill_items = list(SKILLS.items())
    col1, col2 = st.columns(2, gap="medium")
    for i, (group, skills) in enumerate(skill_items):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <div class="skill-card">
                <h4>{group}</h4>
                <div class="skill-tags-grid">{tags_html(skills, "skill-tag")}</div>
            </div>
            """, unsafe_allow_html=True)


def page_projets():
    st.markdown('<p class="section-title">Projets Data</p><div class="section-bar"></div>', unsafe_allow_html=True)
    st.markdown(
        "10 projets issus de la formation **Data Analyst d'OpenClassrooms × ENSAE** "
        "— analyse de données, modélisation SQL, pipelines dbt et dashboards.",
    )

    selected = st.selectbox(
        "Catégorie",
        ["Toutes les catégories"] + ALL_CATEGORIES,
        label_visibility="collapsed",
    )

    filtered = [
        p for p in PROJECTS
        if selected == "Toutes les catégories" or selected in p["categories"]
    ]

    st.markdown('<div style="height:0.75rem"></div>', unsafe_allow_html=True)

    n_cols = 2
    for row_start in range(0, len(filtered), n_cols):
        row = filtered[row_start : row_start + n_cols]
        cols = st.columns(n_cols, gap="medium")
        for col, project in zip(cols, row):
            with col:
                img_tag = (
                    f'<img class="project-img" src="data:image/png;base64,{project["_b64"]}" alt="">'
                    if project["_b64"]
                    else ""
                )
                st.markdown(f"""
                <div class="project-card">
                    {img_tag}
                    <div class="project-body">
                        <p class="project-title">{project["title"]}</p>
                        <p class="project-desc">{project["description"]}</p>
                        {tags_html(project["categories"][:3], "cat-badge")}
                        <p class="tools-line">{project["tools"]}</p>
                        <a class="gh-link" href="{project["url"]}" target="_blank">Voir sur GitHub →</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)


_photo_b64 = _img_b64("photo.jpg")

st.markdown(CSS, unsafe_allow_html=True)

with st.sidebar:
    _photo_tag = (
        f'<div class="sb-photo-wrap"><img class="sb-photo" src="data:image/jpeg;base64,{_photo_b64}" alt=""></div>'
        if _photo_b64 else ""
    )
    st.markdown(f"{_photo_tag}", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
<p class="sb-label">Contact</p>
<p class="sb-value">+33 6 87 15 14 41</p>
<p class="sb-value">josy.elices@gmail.com</p>
<div style="height:0.9rem"></div>
<p class="sb-label">Localisation</p>
<p class="sb-value">Paris, France</p>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Présentation", "Projets Data"])
with tab1:
    page_home()
with tab2:
    page_projets()
