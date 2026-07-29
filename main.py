from repository import search

repo = search.build(".")

print("Classes containing 'agent'")
print("---------------------------")

for symbol in repo.classes("agent"):

    print(
        f"{symbol.name:<25}"
        f"{symbol.file}"
        f":{symbol.line}"
    )

print()

print("Functions containing 'run'")
print("--------------------------")

for symbol in repo.functions("run")[:20]:

    print(
        f"{symbol.name:<25}"
        f"{symbol.file}"
        f":{symbol.line}"
    )

print()

print("Files containing 'scheduler'")
print("----------------------------")

for file in repo.text("scheduler")[:20]:

    print(file)