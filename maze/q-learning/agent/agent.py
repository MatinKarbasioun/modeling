from .q_table import QTable


class Agent:

    def __init__(self, actions, learning_rate=0.9, reward_decay=0.9):
        self.__func_value = QTable(actions, learning_rate, reward_decay)

    def learn(self, current_state, current_action, current_reward, new_state):
        self.__func_value.learn(current_state, current_action, current_reward, new_state)

    def choose_action(self, current_state):
        return self.__func_value.choose_action(current_state)
