from sandbox import (
    workspace,
    executor,
)

root = workspace.create(".")

print()

print("Workspace")

print("---------")

print(root)

print()

result = executor.run(

    ["python", "--version"],

    cwd=root,

)

print(result["stdout"])

workspace.cleanup()