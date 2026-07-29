import json

from core.reasoner import Reasoner
from core.planner import planner
from tools.manager import manager
from memory.manager import memory


class Agent:

    def __init__(self):
        self.reasoner = Reasoner()

    def run(self, prompt):

        memory.remember(prompt)

        thought = self.reasoner.think(prompt)

        reasoning = json.loads(thought)

        print("\n========== REASONING ==========\n")
        print(reasoning["thought"])

        if reasoning["requires_planning"]:

            plan = planner.create(prompt)

            print("\n========== PLAN ==========\n")
            print(plan)

            result = manager.execute(plan)

            memory.remember(str(result))

            return result

        memory.remember(str(reasoning))

        return reasoning


agent = Agent()