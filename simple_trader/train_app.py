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
    agent = Trader(state_size=windows_size, action_size=len(market.actions))

    start_time = time.time()

    for i in range(episode_count + 1):
        print('Episode {}/{}'.format(i, episode_count))
        agent.reset()
        state, price_data = market.reset()

        for t in range(market.last_data_index):
            action, bought_price = agent.decision(state, price_data)
            next_state, next_price_data, reward, done = market.get_next_state_reward(action, bought_price)

            agent.memory.append((state, action, reward, next_state, done))

            if len(agent.memory) > batch_size:
                agent.experience_replay(batch_size)

            state = next_state
            price_data = next_price_data

            if done:
                print("---------------------------------")
                print(f"Total profit: {agent.total_profit}")
                print("---------------------------------")

        if i % 10 == 0:
            if not os.path.exists("models"):
                os.mkdir("models")

            agent.model.save("models/model_ep" + str(i) + ".keras")

    end_time = time.time()
    print("Training time took {} seconds".format(end_time-start_time))


if __name__ == '__main__':
    main()
