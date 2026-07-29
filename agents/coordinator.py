from agents.registry import registry

from agents.chat_agent import agent as chat_agent
from agents.tool_agent import agent as tool_agent
from agents.memory_agent import agent as memory_agent


registry.register(chat_agent)
registry.register(tool_agent)
registry.register(memory_agent)


class Coordinator:

    def execute(self, task: str):

        text = task.lower()

        if any(word in text for word in [
            "calculate",
            "search",
            "find",
            "open",
            "run"
        ]):

            return registry.get("tool").execute(task)

        if any(word in text for word in [
            "remember",
            "memory",
            "recall"
        ]):

            return registry.get("memory").execute(task)

        return registry.get("chat").execute(task)


coordinator = Coordinator()