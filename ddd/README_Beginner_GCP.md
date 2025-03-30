# DDx Beginner Deployment Guide (Google Cloud Edition)

## 1. Set Up
- Create a GCP project
- Enable Kubernetes Engine and Billing

## 2. Install Tools
- Install Google Cloud SDK, Docker, Git

## 3. Create Cluster
```bash
gcloud init
gcloud container clusters create ddx-cluster --zone us-central1-a --num-nodes=2
gcloud container clusters get-credentials ddx-cluster --zone us-central1-a
```

## 4. Build + Push Docker Images
```bash
gcloud auth configure-docker
docker build -t gcr.io/YOUR_PROJECT_ID/ddx-inference:latest -f docker/Dockerfile.inference .
docker push gcr.io/YOUR_PROJECT_ID/ddx-inference:latest
```

## 5. Deploy
```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

## 6. Check Status
```bash
kubectl get pods
```

## 7. Go Live
Set `DDX_LIVE_MODE=1` in .env and restart:
```bash
kubectl rollout restart deployment ddx-inference
```

You're live. Monitor profit. Let AI trade.
