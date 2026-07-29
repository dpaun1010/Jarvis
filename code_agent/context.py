from pathlib import Path

from code_agent.files import project


class ContextBuilder:

    def build(

        self,

        files

    ):

        context = []

        for file in files:

            path = Path(file)

            context.append(

                f"===== {path} ====="

            )

            context.append(

                project.read(path)

            )

        return "\n\n".join(context)


builder = ContextBuilder()