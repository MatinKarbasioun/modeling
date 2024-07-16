from agent import Trader
from environment import Market

import os
import time


def main():
    windows_size = 5
    episode_count = 10
    stock_name = "GSPC_2011"
    batch_size = 32

    market = Market(windows_size=windows_size, ticker=stock_name)
    agent = Trader(windows_size=windows_size, action_size=len(market.actions))

if __name__ == '__main__':
    main()