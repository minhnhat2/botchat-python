import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["my name is (.*)", ["hi %1"]],
    ["hi|hello|hola", ["hello there!", "hi there!"]], 
    ["(.*) age?", ["I am a computer program, I don't have age"]],
    ["(.*) (location|city)", ["I am located in a virtual space"]],
    ["(.*) created?", ["I was created by a team of developers"]],
    ["how (.*) health(.*)", ["I am a computer program, I don't have health"]],
    ["(.*) (sports|game)", ["I am not interested in sports or games"]],
    ["(.*) (movies|films)", ["I love movies! Which is your favorite?"]],
    ["(.*) (book|novel)", ["I love reading books! What's your favorite book?"]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
