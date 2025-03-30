#!/usr/bin/env bash
# rollout.sh - Trigger new model rollout

echo "[DDx] Rolling out new inference model..."
# This is a placeholder; actual steps might involve updating configMap with the new model path
# or re-deploying the ddx-inference deployment with new model image/tag

kubectl rollout restart deployment ddx-inference-deployment
echo "[DDx] Rollout triggered!"
