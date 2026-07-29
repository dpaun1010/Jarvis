from context import context_builder
from patch.models import (
    PatchPlan,
    FileEdit,
    EditType,
)


class PatchPlanner:

    def build(self, objective: str):

        context = context_builder.build(objective)

        plan = PatchPlan(objective)

        for chunk in context.chunks:

            plan.edits.append(

                FileEdit(

                    file=chunk.file,

                    edit_type=EditType.REPLACE,

                    target="",

                    replacement="",

                    reason="Requires analysis",

                )

            )

        return plan


patch_planner = PatchPlanner()