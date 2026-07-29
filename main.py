import tools

from pprint import pprint

from tools.manager import manager

print("\nAvailable Test\n")

print(manager.execute("calculator", "125*10"))

print()

pprint(manager.execute("search", "Latest AI News", 3))