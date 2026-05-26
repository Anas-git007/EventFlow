import numpy as np

def detect_anomalies(df):
    mean = df["energy"].mean()
    std = df["energy"].std()

    df["z_score"] = (df["energy"] - mean) / std
    df["anomaly"] = np.abs(df["z_score"]) > 3

    return df