from chatterbot import ChatBot


# Create a new chat bot
FSU_Chatbot = ChatBot('Bot')

# Loop for conversation
while True:
    try:
        user_input = input("User: ")
        if user_input:
            bot_response = FSU_Chatbot.get_response(user_input)
            print("Bot: ", bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
