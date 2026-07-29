from abc import ABC, abstractmethod


class Plugin(ABC):

    name = ""
    version = "1.0"

    @abstractmethod
    def register(self, registry):
        pass