import json

from ollama import Client
from config import settings


SYSTEM_PROMPT = """
You are the planning engine of DeepJarvis.

Return ONLY valid JSON.

Available tools:

chat
calculator
search
filesystem

Schema:

{
    "steps": [
        {
            "tool": "tool_name",
            "parameters": {}
        }
    ]
}

Examples:

User: Hello

{
    "steps": [
        {
            "tool": "chat",
            "parameters": {
                "prompt": "Hello"
            }
        }
    ]
}

User: Calculate 20*10

{
    "steps": [
        {
            "tool": "calculator",
            "parameters": {
                "expression": "20*10"
            }
        }
    ]
}

User: Search latest AI news

{
    "steps": [
        {
            "tool": "search",
            "parameters": {
                "query": "latest AI news"
            }
        }
    ]
}
"""


class Planner:

    def __init__(self):
        self.client = Client(
            host=settings.ollama_host
        )

        self.model = settings.model

    def create(self, prompt):

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return json.loads(response.message.content)


planner = Planner()