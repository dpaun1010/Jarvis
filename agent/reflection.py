from ollama import Client

from config import settings


SYSTEM = """
You are DeepJarvis.

Your job is to evaluate whether the previous tool result solved the user's goal.

Reply ONLY with JSON.

{
    "completed": true,
    "reason": "..."
}
"""


class ReflectionEngine:

    def __init__(self):

        self.client = Client(
            host=settings.ollama_host
        )

    def reflect(self, goal, result):

        response = self.client.chat(

            model=settings.model,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM
                },
                {
                    "role": "user",
                    "content": f"""
Goal:
{goal}

Result:
{result}
"""
                }
            ]
        )

        return response.message.content


reflection = ReflectionEngine()