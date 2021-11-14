from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
FSU_Chatbot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(FSU_Chatbot)

# Training chat bot with english corpus
trainer.train(
    "chatterbot.corpus.english"
)
