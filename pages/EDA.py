import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="Cars EDA",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
df = pd.read_csv("Cars.csv")

# -------------------------------------------------
# PAGE TITLE
# -------------------------------------------------
st.title("📊 Exploratory Data Analysis")
st.markdown(
    "Explore the Cars dataset using **Univariate, Bivariate "
    "and Multivariate Analysis**."
)

st.divider()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.header("🔍 Analysis Selection")

analysis_type = st.sidebar.radio(
    "Select Analysis",
    [
        "Univariate Analysis",
        "Bivariate Analysis",
        "Multivariate Analysis"
    ]
)

# =================================================
# UNIVARIATE ANALYSIS
# =================================================

if analysis_type == "Univariate Analysis":

    st.header("📌 Univariate Analysis")

    st.write(
        "Univariate analysis studies one variable at a time "
        "to understand its distribution."
    )

    variable = st.selectbox(
        "Select Variable",
        [
            "Location",
            "Fuel_Type",
            "Year",
            "Transmission",
            "Owner_Type",
            "Color",
            "Seats",
            "Doors",
            "Company",
            "Model"
        ]
    )

    st.subheader(f"Distribution of {variable}")

    fig, ax = plt.subplots(figsize=(12, 5))

    value_counts = df[variable].value_counts().head(15)

    value_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel(variable)
    ax.set_ylabel("Number of Cars")
    ax.set_title(f"{variable} Distribution")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    st.info(
        f"The chart above shows the distribution of cars based on "
        f"**{variable}**."
    )


# =================================================
# BIVARIATE ANALYSIS
# =================================================

elif analysis_type == "Bivariate Analysis":

    st.header("📌 Bivariate Analysis")

    st.write(
        "Bivariate analysis studies the relationship between "
        "two variables."
    )

    analysis = st.selectbox(
        "Select Analysis",
        [
            "Location vs Price",
            "Year vs Price",
            "Fuel Type vs Price"
        ]
    )

    # ---------------------------------------------
    # LOCATION VS PRICE
    # ---------------------------------------------

    if analysis == "Location vs Price":

        st.subheader("📍 Location vs Price")

        location_price = (
            df.groupby("Location")["Price"]
            .sum()
            .sort_values(ascending=False)
            .head(15)
        )

        fig, ax = plt.subplots(figsize=(12, 5))

        location_price.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Location")
        ax.set_ylabel("Total Price")
        ax.set_title("Location vs Total Price")

        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

    # ---------------------------------------------
    # YEAR VS PRICE
    # ---------------------------------------------

    elif analysis == "Year vs Price":

        st.subheader("📅 Year vs Price")

        year_price = (
            df.groupby("Year")["Price"]
            .sum()
            .sort_index()
        )

        fig, ax = plt.subplots(figsize=(12, 5))

        year_price.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Year")
        ax.set_ylabel("Total Price")
        ax.set_title("Year vs Total Price")

        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

    # ---------------------------------------------
    # FUEL TYPE VS PRICE
    # ---------------------------------------------

    elif analysis == "Fuel Type vs Price":

        st.subheader("⛽ Fuel Type vs Price")

        fuel_price = (
            df.groupby("Fuel_Type")["Price"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        fuel_price.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Fuel Type")
        ax.set_ylabel("Total Price")
        ax.set_title("Fuel Type vs Total Price")

        plt.xticks(rotation=0)
        plt.tight_layout()

        st.pyplot(fig)


# =================================================
# MULTIVARIATE ANALYSIS
# =================================================

else:

    st.header("📌 Multivariate Analysis")

    st.write(
        "Multivariate analysis studies multiple variables "
        "together to identify meaningful patterns."
    )

    analysis = st.selectbox(
        "Select Analysis",
        [
            "Location + Fuel Type + Price",
            "Transmission + Fuel Type + Average Price",
            "Company + Transmission + Average Price"
        ]
    )

    # ---------------------------------------------
    # LOCATION + FUEL TYPE + PRICE
    # ---------------------------------------------

    if analysis == "Location + Fuel Type + Price":

        st.subheader("📍 Location + Fuel Type + Price")

        data = (
            df.groupby(
                ["Location", "Fuel_Type"]
            )["Price"]
            .sum()
            .unstack()
            .fillna(0)
        )

        data = data.head(15)

        fig, ax = plt.subplots(figsize=(14, 6))

        data.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Location")
        ax.set_ylabel("Total Price")
        ax.set_title(
            "Location + Fuel Type + Total Price"
        )

        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

    # ---------------------------------------------
    # TRANSMISSION + FUEL TYPE + AVERAGE PRICE
    # ---------------------------------------------

    elif analysis == "Transmission + Fuel Type + Average Price":

        st.subheader(
            "⚙️ Transmission + Fuel Type + Average Price"
        )

        data = (
            df.groupby(
                ["Transmission", "Fuel_Type"]
            )["Price"]
            .mean()
            .unstack()
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        data.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Transmission")
        ax.set_ylabel("Average Price")
        ax.set_title(
            "Transmission + Fuel Type + Average Price"
        )

        plt.xticks(rotation=0)
        plt.tight_layout()

        st.pyplot(fig)

    # ---------------------------------------------
    # COMPANY + TRANSMISSION + AVERAGE PRICE
    # ---------------------------------------------

    elif analysis == "Company + Transmission + Average Price":

        st.subheader(
            "🏢 Company + Transmission + Average Price"
        )

        data = (
            df.groupby(
                ["Company", "Transmission"]
            )["Price"]
            .mean()
            .unstack()
        )

        data = data.head(15)

        fig, ax = plt.subplots(figsize=(14, 6))

        data.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Company")
        ax.set_ylabel("Average Price")
        ax.set_title(
            "Company + Transmission + Average Price"
        )

        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    "🚗 Cars Analytics Dashboard | Exploratory Data Analysis"
)