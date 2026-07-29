from automation.workflow import Workflow


class WorkflowManager:

    def __init__(self):

        self.workflows = {}

    def register(self, workflow: Workflow):

        self.workflows[workflow.name] = workflow

    def get(self, name: str):

        return self.workflows.get(name)

    def execute(self, name: str):

        workflow = self.get(name)

        if workflow is None:

            raise ValueError(f"Workflow '{name}' not found.")

        workflow.execute()

    def list(self):

        return list(self.workflows.keys())


manager = WorkflowManager()