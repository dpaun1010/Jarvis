from repository import dependency_graph

graph = dependency_graph.build(".")

print()

print("Dependency Summary")

print("------------------")

print(f"Files: {len(graph.dependencies)}")

print()

for file in list(graph.dependencies.keys())[:10]:

    print(file)

    for dep in graph.imports_of(file):

        print("   ->", dep)

    print()