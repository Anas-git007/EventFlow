import pandas as pd
import numpy as np

def generate_data(n=2000):
    np.random.seed(42)

    data = {
        "timestamp": pd.date_range("2024-01-01", periods=n, freq="min"),
        "energy": np.random.normal(50, 15, n),
        "signal": np.random.normal(100, 20, n),
        "noise": np.random.normal(5, 2, n),
        "detector_id": np.random.randint(1, 6, n)
    }

    df = pd.DataFrame(data)

    # Inject anomalies
    anomaly_indices = np.random.choice(n, 40, replace=False)
    df.loc[anomaly_indices, "energy"] *= np.random.randint(2, 5)

    return df