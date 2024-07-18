import numpy as np

from simple_trader.data.data_reader import DataReader


class Market:
    def __init__(self, windows_size, ticker):
        self.__ticker = ticker
        self.__window_size = windows_size
        self.__data: list = DataReader.read_data(ticker)
        self.__states = self.__data_preprocess()
        self.__actions = ['hold', 'buy', 'sell']
        self.__index = -1
        self.__last_data_index = len(self.__data) - 1

    def __data_preprocess(self):
        pre_processed_data = []

        for t in range(len(self.__data)):
            state = self.__get_state(t)
            pre_processed_data.append(state)

        return pre_processed_data

    def __get_state(self, current_data_index):
        start_index = current_data_index - self.__window_size
        data_block = self.__data[start_index: current_data_index + 1] if start_index >= 0 else (
                -start_index * [self.__data[0]] + self.__data[0: current_data_index + 1])
        result = []
        for i in range(self.__window_size):
            result.append(data_block[i + 1] - data_block[i])

        return np.array([result])

    def reset(self):
        self.__index = -1
        return self.__states[0], self.__data[0]

    def get_next_state_reward(self, action, bought_price=None):
        self.__index += 1

        if self.__index > self.__last_data_index:
            self.__index = 0

        next_state = self.__states[self.__index + 1]
        next_price_data = self.__data[self.__index + 1]

        price_data = self.__data[self.__index]  # current price
        reward = 0

        if action == 2 and bought_price is not None:
            reward = max(price_data - bought_price, 0)

        done = True if self.__index == self.__last_data_index - 1 else False

        return next_state, next_price_data, reward, done

    @property
    def actions(self):
        return self.__actions

    @property
    def last_data_index(self):
        return self.__last_data_index

    @property
    def data(self):
        return self.__data