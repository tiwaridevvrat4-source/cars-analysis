import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Cars Analytics",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# CREATE PAGES
# -----------------------------
home = st.Page(
    "pages/Home.py",
    title="Home",
    icon=":material/home:"
)

EDA = st.Page(
    "pages/eda.py",
    title="EDA",
    icon=":material/bar_chart:"
)

insights = st.Page(
    "pages/2_Insights.py",
    title="Insights",
    icon=":material/lightbulb:"
)
# -----------------------------
# NAVIGATION
# -----------------------------
pg = st.navigation(
    {
        "Cars Analytics": [
            home,
            EDA,
            insights
        
        ]
    }
)

# -----------------------------
# RUN SELECTED PAGE
# -----------------------------
pg.run()