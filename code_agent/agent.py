import json

from code_agent.search import search
from code_agent.context import builder
from code_agent.generator import generator
from code_agent.patcher import patcher
from code_agent.planner import planner


class CodingAgent:

    def execute(

        self,

        root,

        task

    ):

        response = planner.plan(task)

        plan = json.loads(response)

        files = [

            f"{root}/{f}"

            for f in plan["files"]

        ]

        context = builder.build(files)

        for file in files:

            code = generator.generate(

                task,

                context

            )

            patcher.save(

                file,

                code

            )


agent = CodingAgent()