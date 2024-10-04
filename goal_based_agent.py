#!/usr/bin/env python3
"""
Goal-Based Agent in a Grid Environment
"""

import numpy as np

class GoalEnvironment:
    def __init__(self, grid_size=(5, 5), goal_position=[4, 4]):
        self.grid_size = grid_size
        self.agent_position = [0, 0]  # Starting position of the agent
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

class GoalAgent:
    def __init__(self, environment):
        self.environment = environment

    def reach_goal(self):
        while self.environment.agent_position != self.environment.goal_position:
            if self.environment.agent_position[0] < self.environment.goal_position[0]:
                self.environment.move_agent("down")
            elif self.environment.agent_position[0] > self.environment.goal_position[0]:
                self.environment.move_agent("up")
            elif self.environment.agent_position[1] < self.environment.goal_position[1]:
                self.environment.move_agent("right")
            elif self.environment.agent_position[1] > self.environment.goal_position[1]:
                self.environment.move_agent("left")
            self.environment.display_grid()

if __name__ == "__main__":
    env = GoalEnvironment()
    agent = GoalAgent(env)
    agent.reach_goal()
