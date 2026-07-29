from planner.models import (
    ExecutionPlan,
    PlannedFile,
    PlannedStep,
)
from repository import search


class Planner:

    def build(self, objective: str):

        repo = search.build(".")

        plan = ExecutionPlan(
            objective=objective,
            confidence=0.0,
        )

        candidates = set()

        for file in repo.files(objective):
            candidates.add(file)

        for file in repo.text(objective):
            candidates.add(file)

        for path in sorted(candidates):

            plan.files.append(

                PlannedFile(

                    path=path,

                    reason="Matched repository search",

                    confidence=0.90,

                )

            )

        steps = [
            "Inspect repository context",
            "Locate affected symbols",
            "Review dependencies",
            "Generate minimal patch",
            "Validate syntax",
            "Run tests",
            "Reflect on results",
        ]

        for i, step in enumerate(steps, start=1):

            plan.steps.append(

                PlannedStep(

                    order=i,

                    description=step,

                )

            )

        if plan.files:

            plan.confidence = 0.90
        else:
            plan.confidence = 0.25

        return plan


planner = Planner()