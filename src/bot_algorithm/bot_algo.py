import bot_responses.bot_response as br

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainity = 0;
    has_required_words = True;
    
    # Counting certainity
    for word in user_message:
        if word in recognized_words:
            message_certainity += 1
            
    # Calculates percentage
    percentage = float(message_certainity) / float(len(recognized_words))
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
        
    if has_required_words or single_response:
        return(int(percentage * 100))
    else:
        return 0


def check_all_messages(message):
    highest_probability_list = {}
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_probability_list
        highest_probability_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
    # response
    response(br.greetings(), ['hello', 'hi', 'hey'], single_response=True)
    # response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response(br.unknown(), ['how', 'are', 'you', 'doing'], required_words=['how'])
    
    best_match = max(highest_probability_list, key=highest_probability_list.get)
    
    return br.unknown() if highest_probability_list[best_match] < 1 else best_match