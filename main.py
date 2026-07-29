from mcp import manager


manager.connect(

    "filesystem",

    "http://localhost:8000"

)

print()

print(

    manager.execute(

        "filesystem",

        "list_directory",

        {
            "path": "."
        }

    )

)