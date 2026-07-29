from ollama import Client

from config import settings

from memory.context import context
from memory.history import history


SYSTEM = """
You are DeepJarvis.

Use the supplied memories if relevant.

If memories are irrelevant, ignore them.

Be concise and helpful.
"""


class Chat:

    def __init__(self):

        self.client = Client(
            host=settings.ollama_host
        )

    def ask(
        self,
        prompt: str
    ):

        memory = context.retrieve(
            prompt
        )

        messages = [

            {
                "role": "system",
                "content": SYSTEM
            }

        ]

        if memory:

            messages.append(

                {
                    "role": "system",
                    "content": f"Relevant Memory:\n{memory}"
                }

            )

        messages.extend(
            history.all()
        )

        messages.append(

            {
                "role": "user",
                "content": prompt
            }

        )

        response = self.client.chat(

            model=settings.model,

            messages=messages

        )

        answer = response.message.content

        history.add_user(prompt)

        history.add_assistant(answer)

        return answer


chat = Chat()