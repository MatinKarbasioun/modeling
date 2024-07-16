# Maze Problem


# Problem Definition
 This project is a simulation of stock trading using Deep Q-Network (DQN)

# Environment
 Environment consists the stock market and stock price changes  
 Environment consists of a method to get next reward (profit) of total trading based on the bought price and new action

## States
 Stock price changes per each day as a state <br>
 We assume the closing price as a price of each data <br>
 If we have the last 4 days prices then we have 3 states (3 price changes)
 
## Actions
 Actions consist of:<br>
 1- Buy stock  
 2- Sell stock  
 3- Hold stock  
 
## Reward
 Reward in stock trading defines as a gaining profit when the agent sells the stock at the end.  
Only consider positive reward for selling stock, otherwise, receive zero as a reward.


# Agent
The training agent has two methods:

 1- Trade method to buy or sell based on current state and price (in case of sell we need price and return extra parameters)<br>
 2- Experience Learning learns based on the last batch of transitions that are the good actions and reward

The evaluation agent just has a trade method to act in the environment and predict the action based on the given state.

# App
We have a two apps that one of them used for training and the another one use for evaluating method
App.py handle the interactions between agent and perform action on the environment and then get reward 
and then choose new action

