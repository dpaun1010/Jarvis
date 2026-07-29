from llm.chat import chat


SYSTEM = """
You are an expert software engineer.

Return ONLY JSON.

{
    "files":[
        "relative/path.py"
    ]
}
"""


class Planner:

    def plan(

        self,

        task

    ):

        prompt = f"""

Task

{task}

"""

        response = chat.ask(

            SYSTEM + prompt

        )

        return response


planner = Planner()