import uuid

from .Agent import Agent


class Environment:
    def __init__(self):
        self.__agents: list[Agent] = []
        self.__agentCoordination: dict[uuid.UUID, tuple] = {}
        self.__goalsCoordination: list[tuple] = []

    def add_agent(self, agent: Agent, base_coordinate: tuple):
        if self.__agents.count(agent) == 0:
            self.__agents.append(agent)
            self.__agentCoordination.update({agent.id: base_coordinate})

    def remove_agent(self, agent: Agent):
        if self.__agents.count(agent) > 0:
            self.__agents.remove(agent)
            self.__agentCoordination.pop(agent.id, None)

    def update(self, agent_id: str, new_coordinate: tuple) -> None:
        self.__agentCoordination.update({agent_id: new_coordinate})

    def get_coordinate(self, agent_id: uuid.UUID) -> tuple:
        return self.__agentCoordination.get(agent_id, None)

    def set_goal_coordinate(self, goal_coordinate: tuple) -> None:
        if self.__goalsCoordination.count(goal_coordinate) == 0:
            self.__goalsCoordination.append(goal_coordinate)

    def remove_goal_coordinate(self, goal_coordinate: tuple):
        if self.__goalsCoordination.count(goal_coordinate) > 0:
            self.__goalsCoordination.remove(goal_coordinate)

    def is_achieved_goal(self, agent_id: uuid.UUID) -> bool:
        agent_coordinate = self.__agentCoordination.pop(agent_id, None)
        is_achieved = False

        if bool(agent_coordinate):
            is_achieved = bool(list(filter(lambda goal_coordinate: goal_coordinate == agent_coordinate,
                                    self.__goalsCoordination)))

        return is_achieved
