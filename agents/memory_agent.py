from memory.context import context

from agents.base import BaseAgent


class MemoryAgent(BaseAgent):

    name = "memory"

    description = "Memory retrieval"

    def execute(self, task: str):

        return context.retrieve(task)


agent = MemoryAgent()