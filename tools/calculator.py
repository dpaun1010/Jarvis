from tools.base import Tool


class CalculatorTool(Tool):

    name = "calculator"

    description = "Performs mathematical calculations."

    def run(self, expression: str):

        try:
            return eval(expression, {"__builtins__": {}}, {})
        except Exception as e:
            return str(e)