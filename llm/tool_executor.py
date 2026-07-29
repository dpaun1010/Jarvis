from tools.registry import registry


class ToolExecutor:

    def execute(self, tool_name: str, **kwargs):

        tool = registry.get(tool_name)

        if tool is None:

            raise Exception(
                f"Unknown tool: {tool_name}"
            )

        return tool.run(**kwargs)


executor = ToolExecutor()