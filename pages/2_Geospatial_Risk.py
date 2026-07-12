import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load Dataset
df = pd.read_csv("data/infrastructure_projects.csv")

# Page Title
st.title("🗺️ Geospatial Risk Analysis")
st.subheader("Interactive Infrastructure Project Map")

# Filters
sector = st.selectbox(
    "Select Sector",
    ["All"] + list(df["Sector"].unique())
)

risk = st.selectbox(
    "Select Risk Level",
    ["All"] + list(df["Risk_Level"].unique())
)

# Filter Data
filtered_df = df.copy()

if sector != "All":
    filtered_df = filtered_df[
        filtered_df["Sector"] == sector
    ]

if risk != "All":
    filtered_df = filtered_df[
        filtered_df["Risk_Level"] == risk
    ]


# Dashboard Metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Projects",
    len(filtered_df)
)

col2.metric(
    "High Risk Projects",
    len(filtered_df[
        filtered_df["Risk_Level"] == "High"
    ])
)

col3.metric(
    "Average Cost",
    f"${filtered_df['Project_Cost_Million_USD'].mean():.0f} M"
)

# Create Map
m = folium.Map(
    location=[20, 0],
    zoom_start=2
)

colors = {
    "Low": "green",
    "Medium": "orange",
    "High": "red"
}

# Add Markers
for _, row in filtered_df.iterrows():

    folium.Marker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],

        popup=f"""
        <b>{row['Project_Name']}</b><br>
        Country: {row['Country']}<br>
        Sector: {row['Sector']}<br>
        Cost: ${row['Project_Cost_Million_USD']} Million<br>
        Risk Level: {row['Risk_Level']}
        """,

        icon=folium.Icon(
            color=colors[row["Risk_Level"]]
        )

    ).add_to(m)

# Display Map
st_folium(
    m,
    width=1200,
    height=600
)

# Credit Risk Assessment
st.markdown("---")
st.header("🏦 Credit Risk Assessment")

debt_ratio = st.slider(
    "Debt Ratio",
    0.0,
    1.0,
    0.60,
    0.01
)

interest_rate = st.slider(
    "Interest Rate (%)",
    0.0,
    15.0,
    8.0,
    0.1
)

delay = st.slider(
    "Construction Delay (Months)",
    0,
    24,
    6
)

risk_score = (
    debt_ratio * 40 +
    (interest_rate / 15) * 30 +
    (delay / 24) * 30
)

st.metric(
    "Calculated Risk Score",
    f"{risk_score:.1f}/100"
)

if risk_score < 35:
    st.success("🟢 Low Credit Risk")

elif risk_score < 70:
    st.warning("🟠 Medium Credit Risk")

else:
    st.error("🔴 High Credit Risk")