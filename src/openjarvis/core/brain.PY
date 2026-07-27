from ollama import Client

class DeepBrain:
    def __init__(self):
        self.client = Client(host="http://localhost:11434")
        self.model = "qwen3:8b"

    def ask(self, prompt: str):
        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are DeepJarvis, an intelligent personal AI assistant. "
                        "You are professional, concise, technically strong, and proactive."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response["message"]["content"]