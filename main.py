from agents import coordinator


while True:

    task = input("\nYou : ")

    if task.lower() in ["exit", "quit"]:

        break

    print()

    print(

        coordinator.execute(task)

    )