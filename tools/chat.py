from ollama import Client

from tools.base import Tool


class ChatTool(Tool):

    name = "chat"

    description = "General conversation using Ollama."

    def __init__(self):
        self.client = Client(host="http://localhost:11434")
        self.model = "qwen3:8b"

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