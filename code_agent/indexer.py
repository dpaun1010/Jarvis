from code_agent.files import project


class ProjectIndexer:

    def build(self, root):

        index = {}

        for file in project.all(root):

            index[str(file)] = {

                "lines": len(

                    project.read(file).splitlines()

                ),

                "size": file.stat().st_size

            }

        return index


indexer = ProjectIndexer()