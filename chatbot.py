def chatbot():
    print("Welcome to QuickHelp Support Bot!")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("\nYou: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hello! How can I assist you today?")
        
        elif 'product' in user_input:
            print("Bot: We offer electronics, books, and apparel. What are you looking for?")
        
        elif 'price' in user_input or 'cost' in user_input:
            print("Bot: Could you specify the product you're asking about?")
        
        elif 'return' in user_input:
            print("Bot: You can return products within 10 days with the original receipt.")
        
        elif 'support' in user_input or 'help' in user_input:
            print("Bot: Sure! You can call 1800-123-4567 or email support@quickhelp.com.")
        
        elif 'hours' in user_input or 'timing' in user_input:
            print("Bot: We're open from 9 AM to 7 PM, Monday through Saturday.")
        
        elif 'bye' in user_input or 'exit' in user_input:
            print("Bot: Thank you for visiting! Have a great day 😊")
            break
        
        else:
            print("Bot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
