# Deployment-Risk-Assessment-and-Rollback-Prediction

# Deployment Risk Assessment and Rollback Prediction

This project is a prototype system that **analyzes deployment changes**, **predicts the likelihood of a rollback**, and optionally **triggers automated rollbacks** based on anomalies detected post-deployment.

---

## Problem Statement

Modern software deployments often involve multiple services and complex dependencies. Failed deployments can lead to system downtime and user dissatisfaction. This system aims to:

- Predict **deployment risk** using AI/ML models
- Monitor **runtime metrics** after deployment
- Automatically decide whether a **rollback** is needed

---

## Solution Overview

### Core Modules

1. **Deployment Feature Analyzer**  
   Extracts key features from deployment events such as:
   - Deployment time
   - Task count
   - Feature branches
   - Deployment day/hour
   - Failure logs (if any)

2. **Risk Prediction Engine (ML Model)**  
   Uses a trained machine learning model (RandomForest) to predict the risk level (`LOW` or `HIGH`) based on deployment features.

3. **Anomaly Detector**  
   Monitors post-deployment metrics like:
   - CPU usage
   - Memory usage
   - Response time
   - Error rate  
   Detects anomalies using **threshold** or **Z-score** methods.

4. **Rollback Decision Engine**  
   Triggers rollback if:
   - Risk is **high** (`1`)
   - OR anomaly is detected in post-deployment metrics

---

## 📂 Folder Structure

├── main.py # Entry point to run the full pipeline

├── anomaly_detector.py # Anomaly detection module

├── rollback_engine.py # Risk prediction and rollback logic

├── deployment_features.csv # Pipeline-level deployment features

├── monitor_logs/

│ ├── metrics_pipe-risky456.csv # Simulated post-deployment logs

│ └── metrics_pipe-xyz123.csv

├── models/

│ └── deployment_risk_model.pkl # Trained RandomForest model

# OUTPUTS
![image](https://github.com/user-attachments/assets/757bc713-5c7a-4da6-b0b9-9b803a8b2d75)

![image](https://github.com/user-attachments/assets/fa953db7-cf9a-41b8-998d-f83722b2b7e7)



