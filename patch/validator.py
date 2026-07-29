import ast


class PatchValidator:

    def validate_python(
        self,
        source,
    ):

        try:

            ast.parse(source)

            return True, ""

        except SyntaxError as e:

            return False, str(e)


validator = PatchValidator()