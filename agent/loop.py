import json

from agent.state import AgentState
from agent.reflection import reflection
from llm import agent


class AgentLoop:

    def run(self, goal: str) -> AgentState:

        state = AgentState(goal)

        while (
            not state.completed
            and state.iterations < state.max_iterations
        ):

            state.iterations += 1

            result = agent.ask(goal)

            state.add(result)

            response = reflection.reflect(
                goal=goal,
                result=result
            )

            decision = json.loads(response)

            state.completed = decision.get(
                "completed",
                False
            )

        return state


loop = AgentLoop()