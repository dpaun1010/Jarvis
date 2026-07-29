from typing import Dict

from tools.base import Tool


class ToolRegistry:

    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool):
        self._tools[tool.name] = tool

    def unregister(self, name: str):
        self._tools.pop(name, None)

    def get(self, name: str):
        return self._tools.get(name)

    def exists(self, name: str):
        return name in self._tools

    def all(self):
        return list(self._tools.values())

    def names(self):
        return sorted(self._tools.keys())


registry = ToolRegistry()