from repository import call_graph

repo = call_graph.build(".")

print()

print("Repository Graph")
print("----------------")

print("Nodes :", len(repo.nodes))
print("Edges :", len(repo.edges))

print()

count = 0

for symbol in sorted(repo.nodes):

    edges = repo.neighbours(symbol)

    if not edges:
        continue

    print(symbol)

    for edge in edges:

        print(
            "   └──",
            edge.relation,
            edge.target,
        )

    print()

    count += 1

    if count >= 10:
        break