import time

from environment import Environment
from agent import Agent

import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


class App:
    def __init__(self, episode_count):
        self.__episode_count = episode_count
        self.__episodes = range(episode_count)
        self.__rewards = []
        self.__movements = []
        self.__environment = Environment()
        self.__agent = Agent(actions=list(range(self.__environment.action_num)))

    def run_experiment(self):
        start_time = time.time()
        for episode in self.__episodes:
            print(f"Episode {episode}/{self.__episode_count}")
            observation = self.__environment.reset()
            moves = 0

            while True:
                self.__environment.render()
                action = self.__agent.choose_action(str(observation))
                next_observation, reward, done = self.__environment.get_state_reward(action)
                moves += 1

                self.__agent.learn(str(observation), action, reward, str(next_observation))
                observation = next_observation

                if done:
                    self.__movements.append(moves)
                    self.__rewards.append(reward)
                    print(f"Reward: {reward}, Moves: {moves}")
                    break
        end_time = time.time()
        print(f"Game over in {end_time-start_time} seconds!")
        self.__plot_reward_movement()

    def start(self):
        self.__environment.start(self.run_experiment)

    def __plot_reward_movement(self):
        plt.figure()
        plt.subplot(2, 1, 1)

        plt.plot(self.__episodes, self.__movements)
        plt.xlabel('Episodes')
        plt.ylabel('#Movements')

        plt.subplot(2, 1, 2)
        plt.step(self.__episodes, self.__rewards)
        plt.xlabel('Episodes')
        plt.ylabel('#Rewards')

        plt.savefig("Reward_Movement_QLearning.png")
        plt.show()

    @property
    def movements(self):
        return self.__movements


if __name__ == '__main__':
    app = App(50)
    app.start()
