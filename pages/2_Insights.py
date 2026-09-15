import streamlit as st

st.title("💡 Conclusion & Key Insights")

st.markdown("""
This section summarizes the major findings obtained from the
Exploratory Data Analysis of the Cars dataset.
""")

st.divider()

# -----------------------------
# Fuel Type
# -----------------------------

st.header("Fuel Type Insights")

st.write("""
- Petrol and Diesel cars dominate the dataset.
- Diesel cars contribute the highest total sales value.
""")

# -----------------------------
# Transmission
# -----------------------------

st.header("Transmission Insights")

st.write("""
- Manual transmission cars form a larger portion of the dataset
  compared with automatic cars.
""")

# -----------------------------
# Ownership
# -----------------------------

st.header("Ownership Insights")

st.write("""
- First-owner cars represent the largest portion of the dataset.
""")

# -----------------------------
# Colour
# -----------------------------

st.header("Colour Insights")

st.write("""
- White is the most represented car colour in the dataset.
""")

# -----------------------------
# Seats & Doors
# -----------------------------

st.header("Vehicle Configuration")

st.write("""
- 5-seater cars dominate the dataset.
- 4-door and 5-door cars have the highest representation.
""")

# -----------------------------
# Companies
# -----------------------------

st.header("Company Insights")

st.write("""
- Maruti, Hyundai, Honda and Toyota are among the significant
  car manufacturers represented in the dataset.
""")

# -----------------------------
# Location
# -----------------------------

st.header("Location Insights")

st.write("""
- Coimbatore has the highest total car price among the locations
  analyzed.
""")

# -----------------------------
# Year
# -----------------------------

st.header("Year Insights")

st.write("""
- The year 2016 has the highest total sales value in the analysis.
""")

st.divider()

# -----------------------------
# Final Conclusion
# -----------------------------

st.header("🎯 Overall Conclusion")

st.success("""
The EDA provides an overall understanding of the Cars dataset
by examining vehicle characteristics, pricing patterns, fuel types,
transmission, ownership, locations, manufacturing years and
car manufacturers.

The analysis shows that Petrol and Diesel vehicles dominate the
dataset, Manual transmission and First-owner cars have strong
representation, while White and 5-seater cars are highly common.
Location, year and fuel type also show important differences in
total sales value.
""")

st.divider()

st.caption("🚗 Cars Analytics Dashboard | Conclusion & Insights")