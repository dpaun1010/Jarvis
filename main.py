from code_agent import indexer
from code_agent import search

ROOT = "."

print()

print("PROJECT INDEX")

print("----------------")

index = indexer.build(ROOT)

print(

    f"Indexed {len(index)} files."

)

print()

print("SEARCH RESULTS")

print("----------------")

for file in search.find(

    ROOT,

    "class"

):

    print(file)