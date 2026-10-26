from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Interactive Pie Chart")

# Locate data/pie_demo.csv relative to this file, so it works from any launch directory
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "pie_demo.csv"

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error(f"Could not find {DATA_PATH}. Make sure data/pie_demo.csv exists.")
    st.stop()

st.subheader("Data")
st.dataframe(df, use_container_width=True)

# Interactive controls
selected = st.multiselect(
    "Choose categories to include",
    options=df["Category"].tolist(),
    default=df["Category"].tolist(),
)
donut = st.checkbox("Show as donut chart")

filtered = df[df["Category"].isin(selected)]

if filtered.empty:
    st.warning("Select at least one category to display the chart.")
else:
    fig = px.pie(
        filtered,
        names="Category",
        values="Value",
        hole=0.4 if donut else 0,
        title="Spending Breakdown",
    )
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)
