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


def feeling():
    response = ["I'm doing good. What about you?",
                "I'm good. You?",
                "Fine and you?"
                ][random.randrange(3)]
    return response


def neutral():
    response = ["Glad to hear that!",
                "That's good.",
                "Happy to hear that."
                ][random.randrange(3)]
    return response


def question():
    response = ["Oh, why is that?",
                "May I ask why?",
                "Would you tell me more?"
                ][random.randrange(3)]
    return response