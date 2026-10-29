import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time

st.set_page_config(page_title="Denver Weather", page_icon="🌡️", layout="wide")

st.markdown("""
    <style>
      [data-testid="stPlotlyChart"], .stPlotlyChart, .stElementContainer {
        transition: none !important;
        opacity: 1 !important;
      }
    </style>
""", unsafe_allow_html=True)

st.title("🌡️ Denver Temperature Over Time (Open-Meteo)")

lat, lon = 39.7392, -104.9903  # Denver
wurl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"

@st.cache_data(ttl=600)
def get_weather():
    r = requests.get(wurl, timeout=10); r.raise_for_status()
    j = r.json()["current"]
    return pd.DataFrame([{"time": pd.to_datetime(j["time"]),
                          "temperature": j["temperature_2m"],
                          "wind": j["wind_speed_10m"]}])

#refresh
st.subheader("🔁 Auto Refresh Settings")
refresh_sec = st.slider("Refresh every (sec)", 10, 120, 30)
auto_refresh = st.toggle("Enable auto-refresh", value=False)
st.caption(f"Last refreshed at: {time.strftime('%H:%M:%S')}")

#view main
st.subheader("Temperature")

if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["time", "temperature", "wind"])

new = get_weather()
st.session_state.history = pd.concat([st.session_state.history, new]).drop_duplicates(subset="time")
df = st.session_state.history

st.dataframe(df, use_container_width=True)
fig = px.line(df, x="time", y="temperature", markers=True, title="Temperature over time (°C)")
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig, use_container_width=True)

#if refresh wait and then rerun the app.
if auto_refresh:
    time.sleep(refresh_sec)
    get_weather.clear()
    st.rerun()
