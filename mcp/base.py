from abc import ABC, abstractmethod


class MCPServer(ABC):

    name = ""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, tool: str, arguments: dict):
        pass