from llm.chat import chat

from agents.base import BaseAgent


class ChatAgent(BaseAgent):

    name = "chat"

    description = "General conversation"

    def execute(self, task: str):

        return chat.ask(task)


agent = ChatAgent()