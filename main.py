import tools

from tools.registry import registry


print("\nRegistered Tools\n")

for tool in registry.all():

    print(f"✓ {tool.name}")

print()

while True:

    command = input("You : ")

    if command.lower() in ["exit", "quit"]:
        break

    print("DeepJarvis >", command)