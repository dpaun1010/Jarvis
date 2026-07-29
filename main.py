from repository import scanner


files = scanner.scan(".")

print()

print(f"Indexed {len(files)} files\n")

for file in files[:20]:

    print(

        f"{file.path}"

        f" | {file.lines} lines"

        f" | {file.size} bytes"

    )