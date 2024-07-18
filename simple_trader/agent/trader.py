from keras import models
from keras import layers
from keras import optimizers

import numpy as np
import random
from collections import deque


class Trader:
    def __init__(self, state_size, action_size, is_eval=False, model_name=""):
        self.__state_size = state_size
        self.__is_eval = is_eval
        self.__model_name = model_name

        self.__inventory = []
        self.__total_profit = 0
        self.__action_history = []
        self.__action_size = action_size

        self.memory = deque(maxlen=1000)

        # Hyperparameters
        self.__gamma = 0.95
        self.__epsilon = 1.0
        self.__epsilon_min = 0.01
        self.__epsilon_decay = 0.995
        self.__learning_rate = 0.001

        # Model
        self.model: models.Sequential = models.load_model(
            "models/" + model_name) if is_eval else self.__create_model()

    def __create_model(self):
        model = models.Sequential()

        # input layer
        model.add(layers.Dense(units=32, input_dim=self.__state_size, activation='relu'))

        # hidden layer
        model.add(layers.Dense(units=8, activation='relu'))

        # output layer
        model.add(layers.Dense(units=self.__action_size, activation='linear'))

        model.compile(loss='mse', optimizer=optimizers.Adam(learning_rate=self.__learning_rate))
        return model

    def reset(self):  # reset agent after each episode
        self.__inventory = []
        self.__total_profit = 0
        self.__action_history = []

    def decision(self, current_state, price_data):

        """
            if our action is the buy, we add price in inventory to calculate profit later; otherwise,
             if sell we pop that price from inventory
        """

        if not self.__is_eval and np.random.rand() <= self.__epsilon:
            action = random.randrange(self.__action_size)

        else:
            prediction_of_actions = self.model.predict(current_state)  # return probability of each action
            action = np.argmax(prediction_of_actions[0])

        bought_price = None  # just return in sell of position

        if action == 0:  # do noting
            print(".", end="", flush=True)

        elif action == 1:  # buy
            self.__buy(price_data)
            self.__action_history.append(action)

        elif action == 2 and bool(self.__inventory):  # sell
            bought_price = self.__sell(price_data)
            self.__action_history.append(action)

        else:
            self.__action_history.append(0)

        return action, bought_price

    def __buy(self, price_data):
        self.__inventory.append(price_data)
        print(f"Buy: {self.__format_price(price_data)}")

    def __sell(self, price_data):
        bought_price = self.__inventory.pop(0)
        profit = price_data - bought_price
        self.__total_profit += profit
        print(f"Sell: {self.__format_price(price_data)} | Profit: {profit}")
        return bought_price

    @classmethod
    def __format_price(cls, price):
        return ("-$" if price < 0 else "$") + "{0:.2f}".format(abs(price))

    @property
    def total_profit(self):
        return self.__format_price(self.__total_profit)

    def experience_replay(self, batch_size):
        mini_batch = []  # create mini batch to store state-action from previous and create mini-batch from memory
        memory_length = len(self.memory)

        for i in range(memory_length - batch_size + 1, memory_length):
            mini_batch.append(self.memory[i])

        for state, action, reward, next_state, done in mini_batch:
            if done:
                target = reward  # Q-value equal to immediate reward

            else:
                # find Q-value for the next state
                next_q_values = self.model.predict(next_state)[0]
                target = reward + self.__gamma * np.amax(next_q_values)  # bellman equation

            predicated_target = self.model.predict(state)

            # update action-value
            predicated_target[0][action] = target

            # update model input --> state | output --> predicted_target
            self.model.fit(state, predicated_target, epochs=1, verbose=0)

        if self.__epsilon > self.__epsilon_min:  # by going to lower epsilon use predicted instead random action
            self.__epsilon *= self.__epsilon_decay

    @property
    def action_history(self):
        return self.__action_history