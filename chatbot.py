print("================================")
print(" Welcome to DecodeLabs Chatbot ")
print("================================")

print("Type 'exit' anytime to quit.\n")

while True:

    user = input("You: ")

    # Remove spaces and convert to lowercase
    user = user.strip().lower()

    # Greeting
    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! Nice to meet you.")

    # Ask name
    elif user == "what is your name":
        print("Bot: My name is DecodeBot.")

    # Ask how are you
    elif user == "how are you":
        print("Bot: I am doing great. Thank you!")

    # Ask creator
    elif user == "who created you":
        print("Bot: I was created by a DecodeLabs AI Intern.")

    # Goodbye
    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    # Exit command
    elif user == "exit":
        print("Bot: Exiting chatbot...")
        break

    # Unknown message
    else:
        print("Bot: Sorry, I don't understand that.")