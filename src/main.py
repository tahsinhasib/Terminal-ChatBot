import re
from bot_algorithm.bot_algo import check_all_messages



def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Response system
while True:
    print("Bot: " + get_response(input("Me: ")))