import tools

from pprint import pprint

from core.orchestrator import orchestrator


while True:

    prompt = input("\nYou : ")

    if prompt.lower() in ["exit", "quit"]:
        break

    result = orchestrator.run(prompt)

    print()

    pprint(result)