import random

def handle_responses(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "help message"
