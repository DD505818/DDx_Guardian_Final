import gym
import numpy as np

class TradingEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, shape=(10,))
        self.action_space = gym.spaces.Discrete(3) # 0: sell, 1: hold, 2: buy
        self.reset()

    def reset(self):
        self.step_count = 0
        self.profit = 0.
        return self._get_obs()

    def step(self, action):
        # Dummy logic for example
        reward = np.random.normal(1.0, 0.1) if action == 2 else np.random.normal(-0.5, 0.1)
        self.profit += reward
        self.step_count += 1
        done = (self.step_count >= 200)
        return self._get_obs(), reward, done, {}

    def _get_obs(self):
        return np.random.random(10)
