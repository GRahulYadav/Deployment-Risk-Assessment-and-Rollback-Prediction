# anomaly_detector.py

import pandas as pd
import numpy as np

def detect_anomalies(df, method='threshold', thresholds=None, zscore_threshold=2.0):

    if method == 'threshold':
        if thresholds is None:
            thresholds = {
                'cpu_usage': 90,
                'memory_usage': 90,
                'response_time': 600,
                'error_rate': 2.0
            }

        anomalies = pd.DataFrame()
        for col, limit in thresholds.items():
            anomalies[col + '_anomaly'] = df[col] > limit

    elif method == 'zscore':
        anomalies = pd.DataFrame()
        for col in ['cpu_usage', 'memory_usage', 'response_time', 'error_rate']:
            mean = df[col].mean()
            std = df[col].std()
            zscores = (df[col] - mean) / std
            anomalies[col + '_anomaly'] = np.abs(zscores) > zscore_threshold
    else:
        raise ValueError("Invalid method. Choose 'threshold' or 'zscore'.")

    anomalies['any_anomaly'] = anomalies.any(axis=1)

    is_anomaly_detected = anomalies['any_anomaly'].any()
    return is_anomaly_detected, anomalies

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Detect anomalies in deployment metrics.")
    parser.add_argument("--file", type=str, required=True, help="Path to CSV file containing simulated metrics")
    parser.add_argument("--method", type=str, default="threshold", help="Detection method: threshold or zscore")
    args = parser.parse_args()

    df = pd.read_csv(args.file)

    flag, annotated = detect_anomalies(df, method=args.method)
    print(f"Anomaly Detected: {flag}")
    print(annotated.head())
