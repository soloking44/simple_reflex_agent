Simple Reflex Agent Building from Scratch


This project demonstrates how to build different types of intelligent agents from scratch using Python. It walks through several key concepts in artificial intelligence, starting with simple reflex agents and progressing to goal-based and Q-learning agents.

The project is structured into different steps, each corresponding to a specific agent type and their interaction within a grid environment. These agents operate autonomously to navigate their environment and reach a goal.

Project Structure

├── simple_reflex_agent.py  # Implements the Simple Reflex Agent
├── goal_based_agent.py     # Implements the Goal-Based Agent
├── q_learning_agent.py     # Implements the Q-Learning Agent
├── README.md               # Documentation
└── requirements.txt        # Dependencies (if any)

Table of Contents

- Introduction


- Environment Setup


- Agents


- Simple Reflex Agent


- Goal-Based Agent


- Q-Learning Agent


- How to Run the Project

- License

Introduction

- This tutorial focuses on building three types of agents:

1. Simple Reflex Agent – Acts based on current state only, using predefined rules.

2. Goal-Based Agent – Moves towards a goal using logic and strategy to reach a defined objective.


3. Q-Learning Agent – Learns optimal actions through interaction with the environment using reinforcement learning.

- Each agent interacts with a simple grid environment, where it starts at a given location and attempts to navigate the grid to reach a specific goal.

- Environment Setup

- To run this project, you need Python 3 installed on your machine. The project uses basic Python libraries like numpy for handling the grid environment. There are no external dependencies aside from that.

1. Clone the repository:

- git clone https://github.com/soloking44/simple_reflex_agent.git

2. Install dependencies

- pip install numpy matplotlib

3. Make the Python files executable:

- chmod +x simple_reflex_agent.py

- chmod +x goal_based_agent.py

- chmod +x q_learning_agent.py

4. Run Each Script

- You can execute each script as follows:



- Simple Reflex Agent:

- ./simple_reflex_agent.py

- Goal-Based Agent:

- ./goal_based_agent.py

- Q-Learning Agent:

- ./q_learning_agent.py

License

- This project is licensed under the MIT License - see the LICENSE file for details.

Author

- Name: Asakwonye Collins Onyekachi
