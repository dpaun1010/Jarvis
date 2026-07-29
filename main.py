import tools

from agent import loop


while True:

    goal = input("\nGoal : ")

    if goal.lower() in ["exit", "quit"]:
        break

    state = loop.run(goal)

    print()

    print("Iterations :", state.iterations)

    print()

    print("Completed :", state.completed)

    print()

    print("History")

    print("----------------")

    for item in state.history:

        print(item)

        print()