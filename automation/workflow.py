from dataclasses import dataclass, field
from typing import Callable


@dataclass
class WorkflowStep:

    name: str
    action: Callable[[], None]


@dataclass
class Workflow:

    name: str

    steps: list[WorkflowStep] = field(default_factory=list)

    def add_step(self, step: WorkflowStep):

        self.steps.append(step)

    def execute(self):

        print(f"\nStarting Workflow: {self.name}\n")

        for step in self.steps:

            print(f"Running: {step.name}")

            step.action()

        print(f"\nWorkflow '{self.name}' completed.\n")