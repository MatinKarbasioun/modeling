import tkinter as tk # to create windows and widget for our problem
import numpy as np
import time
import sys

UNIT = 40
MAZE_H = 6
MAZE_W = 6
    
    
class Environment:
    def __init__(self):
        self.__window = tk.Tk()
        self.__setup_environment()

    def __setup_environment(self):
        self.__window.title("Maze with Q-Learning")
        self.__window.geometry('{0}x{1}'.format(MAZE_W*UNIT, MAZE_H*UNIT))
        self.__possible_actions = {'u', 'd', 'l', 'r'} 

    @property
    def action_num(self):
        return len(self.__possible_actions)

    def build_env(self):
        self.canvas = tk.Canvas(master=self.__window,
                                background='white',
                                width=MAZE_W*UNIT,
                                height=MAZE_H*UNIT)

        # create vertical lines
        for i in range(0, MAZE_W * UNIT, UNIT):
            x_0, y_0, x_1, y_1 = i, 0, i, MAZE_W * UNIT
            self.canvas.create_line(x_0, y_0, x_1, y_1)

        # Create horizontal lines
        for i in range(0, MAZE_W * UNIT, UNIT):
            x_0, y_0, x_1, y_1 = 0, i, MAZE_H * UNIT, i
            self.canvas.create_line(x_0, y_0, x_1, y_1)

        # Creating the origin of point (start point) (in the middle of the first cell) (we should use pixel number)
        origin = np.array([20, 20]) # each cell has 20 x 20 pixels (so our start point is on the 20 x 20 pixel of whole env)

        # Crating Agent Rectangular
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, 
            origin[1] - 15,
            origin[0] + 15,
            origin[1] + 15,
            fill='red'
        )
        # Creating rectangular hole points
        hole_1_center = origin + np.array([UNIT * 2, UNIT]) # two units to the right and one unit to the down
        hole_2_center = origin + np.array([UNIT, UNIT * 2]) # one units to the right and two unit to the down
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
        goal_cricle_center = origin + np.array([UNIT * 2, UNIT * 2]) # two units to the right and two unit to the down
        self.goal = self.canvas.create_oval(
            goal_cricle_center[0] - 15, 
            goal_cricle_center[1] - 15,
            goal_cricle_center[0] + 15,
            goal_cricle_center[1] + 15,
            fill='yellow' 
        )   
        self.canvas.pack
        
        
if __name__ == "__main__":
    env = Environment()
    env.build_env()
    