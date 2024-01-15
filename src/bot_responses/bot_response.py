import random


def unknown():
    response = ['Please re-phrase that again?',
                '.........',
                "I don't understand",
                "Sorry, can you say that again?"
                ][random.randrange(4)]
    return response

def greetings():
    response = ['Hello there! how can I help you today?',
                'Hi there!',
                "Hey",
                "What's up?"
                ][random.randrange(4)]
    return response

