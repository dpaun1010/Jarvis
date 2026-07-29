from tools.registry import registry


class ToolManager:

    def execute(self, plan):

        outputs = []

        for step in plan["steps"]:

            tool = registry.get(
                step["tool"]
            )

            if tool is None:
                raise Exception(
                    f"{step['tool']} not registered."
                )

            result = tool.run(
                **step["parameters"]
            )

            outputs.append(result)

        return outputs


manager = ToolManager()