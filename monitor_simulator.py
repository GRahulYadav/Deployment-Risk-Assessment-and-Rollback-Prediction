# monitor_simulator.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse
import random
import os

def simulate_metrics(duration_minutes=10, risk_level='low'):
    base_ranges = {
        'low': {
            'cpu': (30, 50),
            'memory': (40, 60),
            'response_time': (100, 200),
            'error_rate': (0.1, 0.5)
        },
        'medium': {
            'cpu': (50, 70),
            'memory': (60, 80),
            'response_time': (200, 400),
            'error_rate': (0.5, 1.5)
        },
        'high': {
            'cpu': (70, 95),
            'memory': (80, 98),
            'response_time': (400, 800),
            'error_rate': (1.5, 5.0)
        }
    }

    if risk_level not in base_ranges:
        raise ValueError("Invalid risk level. Choose from 'low', 'medium', or 'high'.")

    r = base_ranges[risk_level]

    timestamps = [datetime.now() + timedelta(minutes=i) for i in range(duration_minutes)]

    metrics = {
        'timestamp': timestamps,
        'cpu_usage': np.random.uniform(*r['cpu'], size=duration_minutes).round(2),
        'memory_usage': np.random.uniform(*r['memory'], size=duration_minutes).round(2),
        'response_time': np.random.uniform(*r['response_time'], size=duration_minutes).round(2),
        'error_rate': np.random.uniform(*r['error_rate'], size=duration_minutes).round(2),
    }

    return pd.DataFrame(metrics)


def save_metrics(df, pipeline_id=None, output_dir="monitor_logs"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"metrics_{pipeline_id or datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    path = os.path.join(output_dir, filename)
    df.to_csv(path, index=False)
    print(f"Saved simulated metrics to: {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate post-deployment metrics.")
    parser.add_argument("--minutes", type=int, default=15, help="Duration of simulation in minutes")
    parser.add_argument("--risk", type=str, default="low", help="Risk level: low, medium, high")
    parser.add_argument("--pipeline", type=str, default=None, help="Optional pipeline ID")
    args = parser.parse_args()

    df = simulate_metrics(duration_minutes=args.minutes, risk_level=args.risk)
    print(df.head()) 

    save_metrics(df, pipeline_id=args.pipeline)
