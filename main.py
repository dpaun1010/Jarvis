print("Starting DeepJarvis...")

from core.brain import DeepBrain

print("Brain imported successfully.")

brain = DeepBrain()

print("Brain initialized.")

while True:
    question = input("\nYou: ")

    if question.lower() in ("exit", "quit"):
        break

    print("Thinking...")

    answer = brain.ask(question)

    print("\nDeepJarvis:", answer)