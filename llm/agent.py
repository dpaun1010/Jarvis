import json

from ollama import Client

from config import settings

from llm.tool_executor import executor


SYSTEM = """
You are DeepJarvis.

When a tool is required, return ONLY JSON.

Example:

{
    "tool":"calculator",
    "arguments":{
        "expression":"25*8"
    }
}

Otherwise reply normally.
"""


class LLMAgent:

    def __init__(self):

        self.client = Client(
            host=settings.ollama_host
        )

    def ask(self, prompt: str):

        response = self.client.chat(

            model=settings.model,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response.message.content

        try:

            result = json.loads(text)

            return executor.execute(
                result["tool"],
                **result["arguments"]
            )

        except Exception:

            return text


agent = LLMAgent()