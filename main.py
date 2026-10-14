assistant_name = "Eren"

print(f"Hello! I am {assistant_name}.")
print("You can talk to me using commands.")
print("Type 'help' to see what I can do.")

while True:
    command = input("\nYou: ").lower().strip()

    if command == "hello":
        print(f"{assistant_name}: Hello! Nice to meet you.")

    elif command == "how are you":
        print(f"{assistant_name}: I am doing great!")

    elif command == "your name":
        print(f"{assistant_name}: My name is {assistant_name}.")

    elif command == "help":
        print("Available commands: hello, how are you, your name, bye")

    elif command == "bye":
        print(f"{assistant_name}: Goodbye! See you later.")
        break

    else:
        print(f"{assistant_name}: Sorry, I don't understand that command yet.")


