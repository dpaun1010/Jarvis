import tools

from tools.registry import registry

print("Available Tools")
print("----------------")

for tool in registry.all():
    print(f"{tool.name} - {tool.description}")

print("\nCalculator Test")

calc = registry.get("calculator")

print(calc.run("25*8+100"))