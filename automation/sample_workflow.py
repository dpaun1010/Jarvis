from automation.workflow import Workflow
from automation.workflow import WorkflowStep


workflow = Workflow("Morning Routine")


workflow.add_step(

    WorkflowStep(

        "Check Memory",

        lambda: print("Memory Loaded")

    )

)


workflow.add_step(

    WorkflowStep(

        "Start Planner",

        lambda: print("Planner Started")

    )

)


workflow.add_step(

    WorkflowStep(

        "Start Chat",

        lambda: print("Chat Ready")

    )

)