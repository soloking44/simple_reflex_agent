#!/usr/bin/env python3
"""
Q-Learning Agent in a Grid Environment
"""

import numpy as np
import random

class QLearningEnvironment:
    def __init__(self, grid_size=(5, 5), goal_position=[4, 4]):
        self.grid_size = grid_size
        self.agent_position = [0, 0]  # Starting position
        self.goal_position = goal_position

    def display_grid(self):
        grid = np.zeros(self.grid_size)
        grid[self.agent_position[0], self.agent_position[1]] = 1  # Mark agent position
        grid[self.goal_position[0], self.goal_position[1]] = 2    # Mark goal position
        print(grid)

    def move_agent(self, action):
        if action == "up" and self.agent_position[0] > 0:
            self.agent_position[0] -= 1
        elif action == "down" and self.agent_position[0] < self.grid_size[0] - 1:
            self.agent_position[0] += 1
        elif action == "left" and self.agent_position[1] > 0:
            self.agent_position[1] -= 1
        elif action == "right" and self.agent_position[1] < self.grid_size[1] - 1:
            self.agent_position[1] += 1

class QLearningAgent:
    def __init__(self, environment, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.environment = environment
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q_value(self, state, action):
        return self.q_table.get((tuple(state), action), 0.0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(["up", "down", "left", "right"])
        else:
            q_values = {action: self.get_q_value(state, action) for action in ["up", "down", "left", "right"]}
            return max(q_values, key=q_values.get)

    def update_q_value(self, state, action, reward, next_state):
        old_q_value = self.get_q_value(state, action)
        future_reward = max([self.get_q_value(next_state, a) for a in ["up", "down", "left", "right"]])
        new_q_value = (1 - self.alpha) * old_q_value + self.alpha * (reward + self.gamma * future_reward)
        self.q_table[(tuple(state), action)] = new_q_value

    def learn(self, episodes=100):
        for episode in range(episodes):
            state = self.environment.agent_position.copy()
            while state != self.environment.goal_position:
                action = self.choose_action(state)
                self.environment.move_agent(action)
                next_state = self.environment.agent_position.copy()
                reward = 1 if next_state == self.environment.goal_position else -0.1
                self.update_q_value(state, action, reward, next_state)
                state = next_state
                self.environment.display_grid()

if __name__ == "__main__":
    env = QLearningEnvironment()
    agent = QLearningAgent(env)
    agent.learn(episodes=10)
