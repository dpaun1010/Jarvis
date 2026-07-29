from repository import search

search.build(".")

print()

print("Classes")
print("-------")

for cls in search.classes("")[:10]:

    print(cls.name)

    if cls.bases:
        print("  Bases:", ", ".join(cls.bases))

print()

print("Methods")
print("-------")

count = 0

for file in search.repo.files.values():

    for symbol in file.symbols:

        if symbol.kind == "method":

            print(
                f"{symbol.parent}.{symbol.name} "
                f"({symbol.file}:{symbol.line})"
            )

            count += 1

            if count >= 20:
                raise SystemExit