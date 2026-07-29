from mcp.client import MCPClient
from mcp.registry import registry


class MCPManager:

    def connect(
        self,
        name,
        url
    ):

        client = MCPClient()

        client.connect(url)

        registry.register(
            name,
            client
        )

    def execute(
        self,
        server,
        tool,
        arguments
    ):

        client = registry.get(server)

        if client is None:

            raise Exception(
                f"MCP Server '{server}' not found."
            )

        return client.execute(
            tool,
            arguments
        )


manager = MCPManager()