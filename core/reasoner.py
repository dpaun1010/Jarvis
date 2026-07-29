from ollama import Client


SYSTEM_PROMPT = """
You are the reasoning engine of DeepJarvis.

Before answering any request, think carefully.

Return ONLY JSON.

Schema:

{
    "goal":"...",
    "thought":"...",
    "requires_tools":true,
    "requires_planning":true
}
"""


class Reasoner:

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = "qwen3:8b"

    def think(self, prompt):

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

        return response.message.content