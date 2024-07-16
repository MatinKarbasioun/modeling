import uuid
from .AntState import AntState
import numpy as np


class Agent:
    def __init__(self, initial_place:  tuple[int, int], max_axis: tuple[int, int]):
        self.__id: uuid.UUID = uuid.uuid4()
        self.__state: AntState = AntState.SearchForFood
        self.__coordinate: tuple[int, int] = initial_place
        self.__max_axis = max_axis

    @property
    def id(self):
        return self.__id

    def move(self, fermion_value: np.ndarray):
        max_fermion_indices = np.unravel_index(fermion_value.argmax(), fermion_value.shape)
        if max_fermion_indices != (1,1):
            pass

    def __move_up(self):
        new_y = self.__coordinate[1] - 1
        if 0 <= new_y < self.__max_axis[1]:
            self.__coordinate = (self.__coordinate[0], new_y)

    def __move_down(self):
        new_y = self.__coordinate[1] - 1
        if 0 <= new_y < self.__max_axis[1]:
            self.__coordinate = (self.__coordinate[0], new_y)

    def __move_left(self):
        new_x = self.__coordinate[0] + 1
        if 0 <= new_x < self.__max_axis[0]:
            self.__coordinate = (new_x, self.__coordinate[1])

    def __move_right(self):
        new_x = self.__coordinate[0] - 1
        if 0 <= new_x < self.__max_axis[0]:
            self.__coordinate = (new_x, self.__coordinate[1])

    def __move_up_right(self):
        new_x = self.__coordinate[0] + 1
        new_y = self.__coordinate[1] + 1
        if (0 <= new_x < self.__max_axis[0]) and  (0 <= new_y < self.__max_axis[1]):
            self.__coordinate = (new_x, new_y)

    def __move_up_left(self):
        new_x = self.__coordinate[0] - 1
        new_y = self.__coordinate[1] + 1
        if (0 <= new_x < self.__max_axis[0]) and (0 <= new_y < self.__max_axis[1]):
            self.__coordinate = (new_x, new_y)

    def __move_down_right(self):
        new_x = self.__coordinate[0] + 1
        new_y = self.__coordinate[1] - 1
        if (0 <= new_x < self.__max_axis[0]) and (0 <= new_y < self.__max_axis[1]):
            self.__coordinate = (new_x, new_y)

    def __move_down_left(self):
        new_x = self.__coordinate[0] - 1
        new_y = self.__coordinate[1] - 1
        if (0 <= new_x < self.__max_axis[0]) and (0 <= new_y < self.__max_axis[1]):
            self.__coordinate = (new_x, new_y)