# DDx Simplified AI Trading Deployment

Welcome to the beginner-friendly deployment package for **DDx** — your AI-powered crypto trading bot.

## What’s Inside
- `docker/` — Dockerfiles to build inference and training containers
- `scripts/` — Easy one-click deploy scripts
- `k8s/` — Kubernetes files to deploy everything on Google Cloud
- `rl_train_master.py` — Reinforcement learning trainer
- `edge_inference_bridge.py` — ONNX-based fast prediction engine
- `ddx_trading_env.py` — Simulated trading environment
- `README_Beginner_GCP.md` — Full step-by-step guide for beginners

## Quick Start
1. Build Docker images
2. Push to GCR
3. Deploy to GKE using scripts/deploy.sh
4. Monitor with kubectl get pods
5. Edit .env to go live with real capital
