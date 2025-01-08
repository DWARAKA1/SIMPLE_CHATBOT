import spacy
import random
import nltk
from nltk.chat.util import Chat, reflections

# Load SpaCy's pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Download NLTK resources (only needed once)
nltk.download('punkt')

# Define a simple set of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm great, how about you?"]),
    (r"what is your name?", ["I am a chatbot!", "I don't have a name, but you can call me Bot!"]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!"]),
    (r"what is NLP?", ["NLP stands for Natural Language Processing. It is a field of AI that helps computers understand and process human language."]),
    (r"(.*)", ["I'm sorry, I didn't understand that.", "Could you please rephrase?"])
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi! I am your chatbot. Type 'bye' to exit.")  # Initial message
    while True:
        # Take user input
        user_input = input("You: ")

        # If user wants to quit the chat
        if user_input.lower() == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break

        # Get the chatbot's response
        response = chatbot.respond(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
