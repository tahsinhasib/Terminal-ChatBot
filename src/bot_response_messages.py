import random

def unknown():
    response = ['Please re-phrase that again?',
                '.........',
                "I don't understand",
                "Sorry, can you say that again?"
                ][random.randrange(4)]
    
    
    return response