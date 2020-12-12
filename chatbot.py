from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# import en

chatbot = ChatBot('Charlie', read_only=True)

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

while True:
    response = str(input("U: "))
    if response == 'stop':
        break
    response = chatbot.get_response(response)
    print('chatbot: ' + str(response))
