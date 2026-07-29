import tools

from pprint import pprint

from core.planner import planner
from tools.manager import manager


while True:

    prompt = input("\nYou : ")

    if prompt.lower() in ["exit", "quit"]:
        break

    plan = planner.create(prompt)

    print("\nPLAN\n")

    pprint(plan)

    print("\nOUTPUT\n")

    result = manager.execute(plan)

    pprint(result)