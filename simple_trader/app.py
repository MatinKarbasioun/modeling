from keras import models
from matplotlib import pyplot as plt

from agent import Trader
from environment import Market


def main():
    stock_name = 'GSPC_2011_03'
    model_name = "model_ep10"

    model = models.load_model("models/" + model_name)
    windows_size = model.layers[0].input.shape.as_list()[1]

    market = Market(windows_size, stock_name)
    agent = Trader(windows_size, is_eval=True, action_size=len(market.actions), model_name=model_name)

    state, price_data = market.reset()

    for t in range(market.last_data_index):
        action, bought_price = agent.decision(state, price_data)
        next_state, next_price_data, reward, done = market.get_next_state_reward(action, bought_price)

        state = next_state
        price_data = next_price_data

        if done:
            print("---------------------------------")
            print(f"Total profit: {agent.total_profit}")
            print("---------------------------------")

    plot_action_profit(market.data, agent.action_history, agent.total_profit)


def plot_action_profit(data, action_data, profit):
    plt.plot(range(len(data)), data)
    plt.xlabel("date")
    plt.ylabel("price")
    buy, sel = False, False
    for d in range(len(data) - 1):
        if action_data[d] == 1:  # buy
            buy, = plt.plot(d, data[d], 'g*')
        elif action_data[d] == 2:  # sell
            sel, = plt.plot(d, data[d], 'r+')
    if buy and sel:
        plt.legend([buy, sel], ["Buy", "Sell"])
    plt.title("Total Profit: {0}".format(profit))
    plt.savefig("buy_sell.png")
    plt.show()


if __name__ == "__main__":
    main()
