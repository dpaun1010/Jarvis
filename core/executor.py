from tools.manager import manager


class Executor:

    def execute(self, plan):

        outputs = []

        for step in plan["steps"]:

            result = manager.execute({
                "steps": [step]
            })

            outputs.extend(result)

        return outputs


executor = Executor()