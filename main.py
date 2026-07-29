import tools

from pprint import pprint

from core.agent import agent


while True:

    prompt = input("\nYou : ")

    if prompt.lower() in ["exit", "quit"]:
        break

    result = agent.run(prompt)

    print("\n========== RESULT ==========\n")

    pprint(result)