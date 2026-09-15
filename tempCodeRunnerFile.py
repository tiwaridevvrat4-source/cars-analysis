import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cars Analytics Dashboard",
    page_icon="🚗",
    layout="wide"
)

# Load dataset
df = pd.read_csv("Cars.csv")


# =========================
# HOME PAGE
# =========================

def home():

    st.title("🚗 Cars Analytics Dashboard")

    st.subheader("Exploratory Data Analysis & Business Insights")

    st.write("""
    Welcome to the Cars Analytics Dashboard.

    This project performs Exploratory Data Analysis (EDA) on a used-car
    dataset to understand car prices, locations, fuel types, transmission,
    ownership, companies, models and other important characteristics.
    """)

    st.divider()

    st.header("📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Records", df.shape[0])

    with col2:
        st.metric("Total Columns", df.shape[1])

    with col3:
        st.metric("Duplicate Rows", df.duplicated().sum())

    st.divider()

    st.header("🎯 Project Objectives")

    st.markdown("""
    - Analyze car distribution across different locations.
    - Understand fuel type preferences.
    - Analyze manual and automatic transmission.
    - Study car price patterns.
    - Identify popular car companies and models.
    - Analyze ownership patterns.
    - Explore relationships between car attributes and price.
    - Extract meaningful business insights from the data.
    """)

    st.divider()

    st.header("🔍 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )


# =========================
# EDA PAGE
# =========================

def eda():

    st.title("📊 Exploratory Data Analysis")

    st.write("EDA visualizations will be added here.")


# =========================
# INSIGHTS PAGE
# =========================

def insights():

    st.title("💡 Conclusion & Insights")

    st.write("Business insights and conclusions will be added here.")


# =========================
# NAVIGATION
# =========================

pg = st.navigation(
    [
        st.Page(home, title="Home", icon="🏠"),
        st.Page(eda, title="EDA", icon="📊"),
        st.Page(insights, title="Insights", icon="💡")
    ]
)

pg.run()