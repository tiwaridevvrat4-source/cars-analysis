import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Cars Analytics",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("Cars.csv")


# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main-title {
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 19px;
    color: #A7B0C0;
    line-height: 1.6;
    margin-bottom: 30px;
}

.section-title {
    font-size: 28px;
    font-weight: 650;
    margin-top: 20px;
    margin-bottom: 15px;
}

.kpi-card {
    background: #151922;
    border: 1px solid #2A3040;
    border-radius: 14px;
    padding: 22px;
    min-height: 125px;
}

.kpi-label {
    font-size: 15px;
    color: #A7B0C0;
    margin-bottom: 10px;
}

.kpi-value {
    font-size: 32px;
    font-weight: 700;
}

.info-card {
    background: #151922;
    border: 1px solid #2A3040;
    border-radius: 14px;
    padding: 24px;
    min-height: 180px;
}

.info-title {
    font-size: 20px;
    font-weight: 650;
    margin-bottom: 10px;
}

.info-text {
    color: #A7B0C0;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HERO SECTION
# -----------------------------

st.markdown(
    '<div class="main-title">Cars Analytics Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    An Exploratory Data Analysis dashboard designed to uncover
    patterns in car pricing, fuel types, transmission, ownership,
    locations and manufacturers.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# -----------------------------
# KPI SECTION
# -----------------------------

st.markdown(
    '<div class="section-title">Dataset Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Cars</div>
            <div class="kpi-value">{len(df):,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Features</div>
            <div class="kpi-value">{len(df.columns)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Locations</div>
            <div class="kpi-value">{df["Location"].nunique()}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Fuel Types</div>
            <div class="kpi-value">{df["Fuel_Type"].nunique()}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# -----------------------------
# PROJECT OBJECTIVE
# -----------------------------

st.markdown(
    '<div class="section-title">Project Objective</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-card">

    <div class="info-title">Exploring the Cars Dataset</div>

    <div class="info-text">
    The primary objective of this project is to perform Exploratory
    Data Analysis on the Cars dataset and identify meaningful patterns
    related to vehicle characteristics, pricing, fuel type,
    transmission, ownership, location, manufacturing year and
    car manufacturers.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


# -----------------------------
# ANALYSIS COVERED
# -----------------------------

st.markdown(
    '<div class="section-title">Analysis Covered</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="info-card">

        <div class="info-title">Univariate Analysis</div>

        <div class="info-text">
        Analysis of individual variables such as Location,
        Fuel Type, Year, Transmission, Owner Type, Colour,
        Seats, Doors, Company and Model.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="info-card">

        <div class="info-title">Bivariate Analysis</div>

        <div class="info-text">
        Analysis of relationships between variables such as
        Location vs Price, Year vs Price and Fuel Type vs Price.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="info-card">

        <div class="info-title">Multivariate Analysis</div>

        <div class="info-text">
        Analysis involving multiple variables including
        Location, Fuel Type, Transmission, Company and Price.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")
st.divider()

st.caption("Cars Analytics • Exploratory Data Analysis Project")