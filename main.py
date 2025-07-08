import argparse
from rollback_engine import run_pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deployment Risk and Rollback Orchestrator")
    parser.add_argument("--model", type=str, required=True, help="Path to trained model (joblib .pkl)")
    parser.add_argument("--features", type=str, required=True, help="Path to deployment features CSV")
    parser.add_argument("--metrics", type=str, required=True, help="Path to monitoring metrics CSV")
    parser.add_argument("--pipeline", type=str, required=True, help="Pipeline ID to evaluate")

    args = parser.parse_args()
    run_pipeline(args.model, args.features, args.metrics, args.pipeline)
