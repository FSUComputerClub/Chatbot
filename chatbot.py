from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new chat bot
chat_bot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chat_bot)

# Training chat bot with english corpus
trainer.train(
    "chatterbot.corpus.english"
)


# Loop for conversation
while True:
    try:
        user_input = input("User: ")
        bot_response = chat_bot.get_response(user_input)
        print("Bot: ", bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
