from abc import ABC, abstractmethod
from typing import Any


class Tool(ABC):
    """
    Base class for every DeepJarvis tool.
    """

    name: str = ""
    description: str = ""

    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        pass

    def __str__(self):
        return self.name
    