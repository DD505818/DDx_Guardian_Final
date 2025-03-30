#!/usr/bin/env python3
import sys
import onnx
import torch
import gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

from ddx_trading_env import TradingEnv

def main():
    episodes = 50000
    model_out = "ddx_model.onnx"
    if "--episodes" in sys.argv:
        idx = sys.argv.index("--episodes") + 1
        episodes = int(sys.argv[idx])
    if "--model_out" in sys.argv:
        idx = sys.argv.index("--model_out") + 1
        model_out = sys.argv[idx]

    # 1. Setup environment
    env = DummyVecEnv([lambda: TradingEnv()])

    # 2. Train PPO
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=episodes)

    # 3. Export to ONNX
    import torch
    obs = env.reset()
    dummy_input = torch.tensor(obs, dtype=torch.float32)
    torch.onnx.export(
        model.policy,
        dummy_input,
        model_out,
        export_params=True,
        opset_version=13,
        do_constant_folding=True,
        input_names=["obs"],
        output_names=["action", "value"],
    )

    print(f"[DDx RL Train] Model saved to {model_out}")

if __name__ == "__main__":
    main()
