from core.brain import DeepBrain


print("="*60)
print("🤖 DeepJarvis v1.0")
print("="*60)

brain = DeepBrain()

while True:

    question = input("\nYou : ")

    if question.lower() in ["exit","quit"]:
        break

    print("\nThinking...")

    answer = brain.ask(question)

    print("\nDeepJarvis :", answer)
