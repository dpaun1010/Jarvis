from llm import chat


while True:

    prompt = input("\nYou : ")

    if prompt.lower() in ["exit", "quit"]:

        break

    print()

    print(

        chat.ask(prompt)

    )