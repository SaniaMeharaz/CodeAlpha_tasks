def chatbot():
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }
    
    print("Chatbot: Type something (type 'bye' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: I don't understand that.")

chatbot()
