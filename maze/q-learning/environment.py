import tkinter as tk  # to create windows and widget for our problem
import numpy as np
import time
import sys

UNIT = 40
MAZE_H = 6
MAZE_W = 6


class Environment:
    def __init__(self):
        self.window = tk.Tk()
        self.__setup_environment()
        self.__build_env()

    def __setup_environment(self):
        self.window.title("Maze with Q-Learning")
        self.window.geometry('{0}x{1}'.format(MAZE_W * UNIT, MAZE_H * UNIT))
        self.__possible_actions = {'u', 'd', 'l', 'r'}

    @property
    def action_num(self):
        return len(self.__possible_actions)

    def __build_env(self):
        self.canvas = tk.Canvas(master=self.window,
                                background='white',
                                width=MAZE_W * UNIT,
                                height=MAZE_H * UNIT)

        # create vertical lines
        for i in range(0, MAZE_W * UNIT, UNIT):
            x_0, y_0, x_1, y_1 = i, 0, i, MAZE_W * UNIT
            self.canvas.create_line(x_0, y_0, x_1, y_1)

        # Create horizontal lines
        for i in range(0, MAZE_W * UNIT, UNIT):
            x_0, y_0, x_1, y_1 = 0, i, MAZE_H * UNIT, i
            self.canvas.create_line(x_0, y_0, x_1, y_1)

        # Creating the origin of point (start point) (in the middle of the first cell) (we should use pixel number)
        origin = np.array(
            [20, 20])  # each cell has 20 x 20 pixels (so our start point is on the 20 x 20 pixel of whole env)

        # Crating Agent Rectangular
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15,
            origin[1] - 15,
            origin[0] + 15,
            origin[1] + 15,
            fill='red'
        )
        # Creating rectangular hole points
        hole_1_center = origin + np.array([UNIT * 2, UNIT])  # Two units to the right and one unit to the down
        hole_2_center = origin + np.array([UNIT, UNIT * 2])  # One units to the right and two unit to the down
        self.hole_1 = self.canvas.create_rectangle(
            hole_1_center[0] - 15,
            hole_1_center[1] - 15,
            hole_1_center[0] + 15,
            hole_1_center[1] + 15,
            fill='black'
        )
        self.hole_2 = self.canvas.create_rectangle(
            hole_2_center[0] - 15,
            hole_2_center[1] - 15,
            hole_2_center[0] + 15,
            hole_2_center[1] + 15,
            fill='black'
        )

        # Create circular objective
        goal_circle_center = origin + np.array([UNIT * 2, UNIT * 2])  # two units to the right and two unit to the down
        self.goal = self.canvas.create_oval(
            goal_circle_center[0] - 15,
            goal_circle_center[1] - 15,
            goal_circle_center[0] + 15,
            goal_circle_center[1] + 15,
            fill='yellow'
        )

        self.canvas.pack()

    def render(self):
        time.sleep(0.1)
        self.window.update()

    def reset(self):
        self.window.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15,
            origin[1] - 15,
            origin[0] + 15,
            origin[1] + 15,
            fill='red'
        )
        return self.canvas.coords(self.rect)

    def get_state_reward(self, action):
        new_state = self.__update_state(action)
        s_, reward, done = self.__get_reward(new_state)
        return s_, reward, done

    def __update_state(self, action):
        current_state = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])

        if action == 0:  # U
            if current_state[1] > UNIT:
                base_action[1] -= UNIT

        elif action == 1:  # D
            if current_state[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT

        elif action == 2:  # R
            if current_state[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT

        elif action == 3:  # L
            if current_state[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])

        new_state = self.canvas.coords(self.rect)
        return new_state

    def __get_reward(self, new_state):
        if new_state in [self.canvas.coords(self.hole_1), self.canvas.coords(self.hole_2)]:
            reward = -1
            done = True
            s_ = 'terminal'

        elif new_state == self.canvas.coords(self.goal):
            s_ = 'terminal'
            done = True
            reward = 1

        else:
            done = False
            reward = 0
            s_ = new_state

        return s_, reward, done

    def start(self, exp_func):
        self.window.after(10, exp_func)
        self.window.mainloop()


if __name__ == "__main__":
    env = Environment()
    env.window.mainloop()
