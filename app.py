import streamlit as st
import pandas as pd
import time
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🔍 Real-Time Log Anomaly Detection System")

# ======================
# Upload Log File
# ======================

uploaded_file = st.file_uploader(
    "Upload System Log File",
    type=["log", "txt"]
)

# ======================
# Parse Logs Automatically
# ======================

def parse_logs(file):

    logs = file.read().decode().splitlines()

    config = TemplateMinerConfig()
    miner = TemplateMiner(config=config)

    data = []

    for i, log in enumerate(logs):

        result = miner.add_log_message(log)

        template = result["template_mined"]

        data.append([
            i,
            len(log),
            1 if "error" in log.lower() else 0,
        ])

    df = pd.DataFrame(
        data,
        columns=["block_id", "avg_length", "has_error"]
    )

    df["count"] = 1

    return df


# ======================
# Dashboard
# ======================

if uploaded_file:

    st.success("✅ Log file uploaded")

    with st.spinner("Parsing logs..."):
        df = parse_logs(uploaded_file)

    st.subheader("Parsed Features")
    st.dataframe(df.head())

    # ======================
    # Train Model
    # ======================

    X = df[["avg_length", "has_error", "count"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = IsolationForest(contamination=0.1)
    df["Prediction"] = model.fit_predict(X_scaled)

    df["Prediction"] = df["Prediction"].map(
        {1: "Normal", -1: "Anomaly"}
    )

    # ======================
    # PCA Visualization
    # ======================

    pca = PCA(n_components=2)
    components = pca.fit_transform(X_scaled)

    vis_df = pd.DataFrame({
        "PC1": components[:, 0],
        "PC2": components[:, 1],
        "Prediction": df["Prediction"]
    })

    st.subheader("📊 PCA Visualization")

    fig = px.scatter(
        vis_df,
        x="PC1",
        y="PC2",
        color="Prediction"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ======================
    # Live Streaming Detection
    # ======================

    st.subheader("⚡ Live Streaming Anomaly Alerts")

    placeholder = st.empty()

    for i in range(len(df)):

        row = df.iloc[i]

        if row["Prediction"] == "Anomaly":
            placeholder.error(
                f"🚨 Anomaly Detected at Log {row['block_id']}"
            )
        else:
            placeholder.success(
                f"✅ Normal Log {row['block_id']}"
            )

        time.sleep(0.1)