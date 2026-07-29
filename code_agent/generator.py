from llm.chat import chat


class Generator:

    def generate(

        self,

        instruction,

        context

    ):

        prompt = f"""

You are modifying an existing project.

Instruction:

{instruction}

Project Context:

{context}

Return ONLY the updated source code.

"""

        return chat.ask(prompt)


generator = Generator()