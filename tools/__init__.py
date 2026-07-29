from tools.registry import registry

from tools.chat import ChatTool
from tools.calculator import CalculatorTool
from tools.search import SearchTool
from tools.filesystem import FileSystemTool

registry.register(ChatTool())
registry.register(CalculatorTool())
registry.register(SearchTool())
registry.register(FileSystemTool())