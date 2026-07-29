from llm.agent import agent as llm_agent

from agents.base import BaseAgent


class ToolAgent(BaseAgent):

    name = "tool"

    description = "Tool execution"

    def execute(self, task: str):

        return llm_agent.ask(task)


agent = ToolAgent()