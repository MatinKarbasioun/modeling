# Maze Problem

# Problem Definition
 This project is a simulation of a maze problem in that there is an agent which was located in the top-right
 corner of the environment. Furthermore, there are two holes at the maze environment that they cover the objective.

# Environment
Maze environment has a method to return state reward based on each action (a)
Environment consists of (6 x 6) tiles and 2 black holes (agent start from most top-right cell and agent would avoid holes)

![maze.PNG](maze.PNG)

## States
  States consist of the coordination of each tile in the board

## Actions
 Agent can move in 4 directions: (**L**)eft, (**R**)ight, (**U**)p, (**D**)ow, therefore actions consist of [L, R, U, D]
## Reward
 +1 for gold hole (objective), -1 for black holes, 0 for the rest states


# Agent
Agent has two methods:

 1- choose_action to choose an action based on the current state (s)

 2- learn based on (the current state, the current action, the immediate reward, and the next state)

# App
App.py handle the interactions between agent and perform action on the environment and then get reward and then choose new action
App use Agent and Environment that represented agent and environment respectively.
