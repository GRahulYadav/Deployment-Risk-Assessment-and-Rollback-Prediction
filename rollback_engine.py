import pandas as pd
import joblib
from anomaly_detector import detect_anomalies

def load_model(model_path):
    return joblib.load(model_path)

def load_pipeline_features(pipeline_feature_file):
    return pd.read_csv(pipeline_feature_file)

def load_monitor_metrics(monitor_file):
    return pd.read_csv(monitor_file)

def predict_risk(model, pipeline_features):
    return model.predict(pipeline_features)[0]

def should_rollback(risk_prediction, anomaly_flag):
    return risk_prediction == 1 or bool(anomaly_flag)

def rollback_action(pipeline_id):
    print(f"\nROLLBACK TRIGGERED for Pipeline: {pipeline_id} ")

def run_pipeline(model_path, feature_file, metrics_file, pipeline_id):
    model = load_model(model_path)
    df_features = load_pipeline_features(feature_file)

    if pipeline_id not in df_features['pipeline_id'].values:
        print(f"\nError: Pipeline ID '{pipeline_id}' not found in feature dataset.")
        return

    row = df_features[df_features['pipeline_id'] == pipeline_id]
    X = row.drop(columns=['pipeline_id'])

    # Check feature alignment
    expected = set(model.feature_names_in_)
    actual = set(X.columns)
    if expected != actual:
        print("\nError: Feature mismatch between input and model.")
        print(f"Features required by model: {sorted(expected)}")
        print(f"Features in input:          {sorted(actual)}")
        if missing := expected - actual:
            print(f"Missing features: {missing}")
        if extra := actual - expected:
            print(f"Extra features not used by model: {extra}")
        return

    risk = predict_risk(model, X)
    print(f"\nML Risk Prediction: {'HIGH' if risk == 1 else 'LOW '}")

    df_metrics = load_monitor_metrics(metrics_file)
    anomaly_flag, _ = detect_anomalies(df_metrics, method='threshold')
    print(f"Anomaly Detected: {'YES' if anomaly_flag else 'NO '}")

    print(f"\nDebug — Risk Value: {risk}, Anomaly Flag: {anomaly_flag}, Type: {type(anomaly_flag)}")

    if should_rollback(risk, anomaly_flag):
        rollback_action(pipeline_id)
    else:
        print(f"\nDeployment for {pipeline_id} is considered STABLE. No rollback needed.")
