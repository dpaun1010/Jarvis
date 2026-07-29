from code_agent.files import project


class CodeEditor:

    def replace(

        self,

        file,

        old,

        new

    ):

        text = project.read(file)

        text = text.replace(

            old,

            new

        )

        project.write(

            file,

            text

        )


editor = CodeEditor()