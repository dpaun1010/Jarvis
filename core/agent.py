import json

from core.reasoner import Reasoner
from core.planner import planner
from tools.manager import manager


class Agent:

    def __init__(self):

        self.reasoner = Reasoner()

    def run(self, prompt):

        thought = self.reasoner.think(prompt)

        reasoning = json.loads(thought)

        print("\n========== REASONING ==========\n")
        print(reasoning["thought"])

        if reasoning["requires_planning"]:

            plan = planner.create(prompt)

            print("\n========== PLAN ==========\n")
            print(plan)

            result = manager.execute(plan)

            return result

        return reasoning


agent = Agent()