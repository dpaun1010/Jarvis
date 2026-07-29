from llm.tool_schema import ToolSchema
from tools.registry import registry


class ToolConverter:

    def convert(self):

        schemas = []

        for tool in registry.all():

            schemas.append(
                ToolSchema(
                    name=tool.name,
                    description=tool.description
                )
            )

        return schemas


converter = ToolConverter()