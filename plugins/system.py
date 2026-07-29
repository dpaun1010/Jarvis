from plugins.base import Plugin

from tools.calculator import CalculatorTool
from tools.search import SearchTool
from tools.filesystem import FileSystemTool
from tools.chat import ChatTool


class SystemPlugin(Plugin):

    name = "system"

    def register(self, registry):

        registry.register(ChatTool())
        registry.register(CalculatorTool())
        registry.register(SearchTool())
        registry.register(FileSystemTool())


plugin = SystemPlugin()