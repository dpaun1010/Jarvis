from abc import ABC, abstractmethod


class BaseAgent(ABC):

    name = ""

    description = ""

    @abstractmethod
    def execute(self, task: str):
        pass