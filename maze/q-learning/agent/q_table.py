import numpy as np
import pandas as pd


class QTable:
    def __init__(self, actions, learning_rate=0.9, reward_decay=0.9, e_greedy=0.1):
        self.__actions = actions
        self.__learning_rate = learning_rate
        self.__gamma = reward_decay
        self.__epsilon = e_greedy
        self.__q_table = pd.DataFrame(columns=self.__actions, dtype=np.float64)

    def __add_state(self, state):
        if state not in self.__q_table.index:
            self.__q_table.loc[state, :] = pd.Series([0] * len(self.__actions), index=self.__q_table.columns)

    def choose_action(self, observation_state):
        self.__add_state(observation_state)
        if self.__random_action():
            action = np.random.choice(self.__actions)

        else:
            state_action = self.__q_table.loc[observation_state, :]
            state_actin = state_action.reindex(np.random.permutation(state_action.index))
            action = state_actin.idxmax()

        return action

    def __random_action(self):
        if np.random.uniform() < self.__epsilon:
            return True

    def learn(self, current_state, current_action, current_reward, new_state):
        self.__add_state(new_state)
        current_q_value = self.__q_table.loc[current_state, current_action]
        max_new_state_q_value = self.__q_table.loc[new_state, :].max()

        if new_state != 'terminal':
            q_target = current_reward + self.__gamma * max_new_state_q_value

        else:
            q_target = current_reward

        self.__q_table.loc[current_state, current_action] += self.__learning_rate * (q_target - current_q_value)

    @property
    def q_table(self):
        return self.__q_table
