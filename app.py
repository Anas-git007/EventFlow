import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from data_generator import generate_data
from anomaly import detect_anomalies
from analytics import basic_stats, time_series, detector_analysis

st.set_page_config(page_title="EventFlow", layout="wide")

st.title("⚛️ EventFlow: Scientific Event Stream Analytics System")

# Generate Data
df = generate_data()
df = detect_anomalies(df)

# Sidebar
st.sidebar.header("Controls")
show_data = st.sidebar.checkbox("Show Raw Data")
show_anomalies = st.sidebar.checkbox("Show Anomalies Only")

# -----------------------
# RAW DATA
# -----------------------
if show_data:
    st.subheader("📊 Raw Event Data")
    st.dataframe(df)

# -----------------------
# ANOMALIES
# -----------------------
st.subheader("⚠️ Detected Anomalies")

anomalies = df[df["anomaly"] == True]
st.write(f"Total anomalies detected: {len(anomalies)}")

fig = px.scatter(
    df,
    x="timestamp",
    y="energy",
    color="anomaly",
    title="Energy Over Time with Anomalies"
)
st.plotly_chart(fig, use_container_width=True)

# -----------------------
# STATISTICS
# -----------------------
st.subheader("📈 Statistical Overview")
st.dataframe(basic_stats(df))

# -----------------------
# TIME SERIES
# -----------------------
st.subheader("⏱️ Time-Series Analysis")

ts = time_series(df)
st.line_chart(ts)

# -----------------------
# DETECTOR ANALYSIS
# -----------------------
st.subheader("🔬 Detector Performance")

det = detector_analysis(df)
st.bar_chart(det)

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.markdown("Built as a research-inspired data analytics system for scientific event streams.")