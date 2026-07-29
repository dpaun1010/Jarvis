import tools

from llm import agent


while True:

    prompt = input("\nYou : ")

    if prompt.lower() in ["exit", "quit"]:
        break

    print()

    print(agent.ask(prompt))