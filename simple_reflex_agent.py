#!/usr/bin/env python3
"""
Simple Reflex Agent in a Grid Environment
"""

import numpy as np

class Environment:
    def __init__(self, grid_size=(5, 5)):
        self.grid_size = grid_size
        self.agent_position = [0, 0]  # Starting position of the agent (top-left corner)

    def display_grid(self):
        grid = np.zeros(self.grid_size)
        grid[self.agent_position[0], self.agent_position[1]] = 1  # Mark agent position
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

class Agent:
    def __init__(self, environment):
        self.environment = environment

    def act(self, action):
        self.environment.move_agent(action)
        self.environment.display_grid()

if __name__ == "__main__":
    env = Environment()
    agent = Agent(env)
    agent.act("down")
    agent.act("right")
