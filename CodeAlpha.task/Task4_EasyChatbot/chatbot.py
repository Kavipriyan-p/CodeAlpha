
print("Welcome to the Simple Chatbot! Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you today?")
    elif "name" in user_input:
        print("Chatbot: I'm a simple chatbot made for the CodeAlpha internship task.")
    elif "help" in user_input:
        print("Chatbot: I can answer basic questions. Try asking about my name or say hello!")
    else:
        print("Chatbot: Sorry, I didn't understand that.")
