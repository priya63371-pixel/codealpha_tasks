def chatbot(message):
    message = message.lower()

    if message == "hello":
        return "Hi!"
   

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "My name is Python chatbot"
    elif message == "thank you chatbot":
        return "You'r Welcome"

    elif message == "bye":
        return "Have a Nice Day!"

    else:
        return "Sorry, I don't understand."

print("Welcome to Simple Chatbot!")

while True:
    user = input("You: ")

    reply = chatbot(user)
    print("Bot:", reply)

    if user.lower() == "bye":
        break