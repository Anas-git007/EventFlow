import pandas as pd

def basic_stats(df):
    return df.describe()

def time_series(df):
    return df.groupby(df["timestamp"].dt.hour)["energy"].mean()

def detector_analysis(df):
    return df.groupby("detector_id")["energy"].mean()