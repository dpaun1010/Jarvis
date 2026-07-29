from core.conversation import conversation
from core.planner import planner
from core.executor import executor


class Orchestrator:

    def run(self, prompt):

        conversation.add_user(prompt)

        plan = planner.create(prompt)

        result = executor.execute(plan)

        conversation.add_assistant(str(result))

        return result


orchestrator = Orchestrator()