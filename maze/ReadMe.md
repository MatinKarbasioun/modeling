## Maze Problem
# States
 tiles (6*6) (two black holse) (agent start from most top-right cell and agent would avoid holes)
# tions
 Move (L)eft, (R)ight, (U)p, (D)own
# Reward
 +1 for gold hole (objective), -1 for black holes, 0 for the rest states

App use RL_agent and Maze_env that represented agent and environment respectively.

## Agent
Agent has two methods:
 1- choose_action to choose action based on state (s)
 2- learn based on (s: current state, a: current action, r: current reward, s_: next state)

## Environment
Maze environment has a method to return state reward based on each action (a)

App.py handle the interactions between agent and perform action on the environment and then get reward and then choose new action



