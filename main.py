from context import context_builder

package = context_builder.build("scheduler")

print()

print("Context Package")
print("----------------")

print("Objective:", package.objective)

print()

print("Files")

print("-----")

for chunk in package.chunks:

    print(chunk.file)

    print("Reason :", chunk.reason)

    print("Lines  :", len(chunk.source.splitlines()))

    print()