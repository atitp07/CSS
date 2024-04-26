# Define responses for the chatbot
responses = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "bye": "Goodbye! Have a great day.",
    "": "Sorry, I didn't understand that."
}

# Function to handle user input and provide responses
def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye! See you next time.")
            break
        response = responses.get(user_input, responses[""])
        print("Chatbot:", response)

# Start the chatbot
print("Chatbot: Hello! I'm your personal assistant chatbot.")
chatbot()