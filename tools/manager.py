from typing import Any

from tools.registry import registry


class ToolManager:

    def execute(self, tool_name: str, *args, **kwargs) -> Any:

        tool = registry.get(tool_name)

        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not found.")

        return tool.run(*args, **kwargs)


manager = ToolManager()