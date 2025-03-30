#!/usr/bin/env bash
# deploy.sh - One-click deployment

echo "[DDx] Building Docker images..."
docker build -t yourregistry.com/ddx-rl-train:latest -f docker/Dockerfile.rl_train .
docker push yourregistry.com/ddx-rl-train:latest

docker build -t yourregistry.com/ddx-inference:latest -f docker/Dockerfile.inference .
docker push yourregistry.com/ddx-inference:latest

echo "[DDx] Applying K8s manifests..."
kubectl apply -f k8s/ddx-federated-backend.yaml
kubectl apply -f k8s/ddx-redis.yaml
kubectl apply -f k8s/ddx-agents.yaml
kubectl apply -f k8s/ddx-frontend.yaml
kubectl apply -f k8s/ddx-ingress.yaml
kubectl apply -f k8s/ddx-hpa.yaml
kubectl apply -f k8s/ddx-cronjob.yaml

echo "[DDx] Deployment complete!"
