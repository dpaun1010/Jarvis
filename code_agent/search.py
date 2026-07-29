from code_agent.files import project


class CodeSearch:

    def find(

        self,

        root,

        keyword

    ):

        results = []

        for file in project.all(root):

            try:

                text = project.read(file)

            except Exception:

                continue

            if keyword.lower() in text.lower():

                results.append(str(file))

        return results


search = CodeSearch()   