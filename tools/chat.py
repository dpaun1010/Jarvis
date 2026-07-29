from ollama import Client

from config import settings
from tools.base import Tool


class ChatTool(Tool):

    name = "chat"

    description = "General conversation using Ollama."

    def __init__(self):
        from config import settings

        self.client = Client(host=settings.ollama_host)
        self.model = settings.model

    def run(self, prompt: str):

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are DeepJarvis, an intelligent AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content

    