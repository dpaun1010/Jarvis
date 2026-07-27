from pathlib import Path

PROJECT = Path(".")

FOLDERS = [
    "core",
    "voice",
    "memory",
    "automation",
    "integrations",
    "plugins",
    "prompts",
    "config",
    "logs",
    "ui",
]


def create_folders():
    for folder in FOLDERS:
        (PROJECT / folder).mkdir(parents=True, exist_ok=True)


def write(path, content):
    path = PROJECT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def create_core():

    write(
        "core/__init__.py",
        ""
    )

    write(
        "core/brain.py",
'''from ollama import Client


class DeepBrain:

    def __init__(self):
        self.client = Client(host="http://localhost:11434")
        self.model = "qwen3:8b"

    def ask(self, prompt):

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role":"system",
                    "content":"You are DeepJarvis, a professional AI assistant."
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response.message.content
'''
    )


def create_main():

    write(
        "main.py",
'''from core.brain import DeepBrain


print("="*60)
print("🤖 DeepJarvis v1.0")
print("="*60)

brain = DeepBrain()

while True:

    question = input("\\nYou : ")

    if question.lower() in ["exit","quit"]:
        break

    print("\\nThinking...")

    answer = brain.ask(question)

    print("\\nDeepJarvis :", answer)
'''
    )


def create_requirements():

    write(
        "requirements.txt",
'''ollama
httpx
pydantic
'''
    )


def main():

    print("\\nCreating DeepJarvis...")

    create_folders()

    create_core()

    create_main()

    create_requirements()

    print("\\n✅ DeepJarvis Ready!")


if __name__ == "__main__":
    main()