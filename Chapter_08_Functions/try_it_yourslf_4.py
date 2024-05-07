

import os 
os.system('clear')

def display_message(orginal_message, printed_message):
    """ Displays all the message from one list."""
    print('\n\n')
    while orginal_message:
        current_message = orginal_message.pop()
        print(f"Printing Message :{current_message}")
        printed_message.append(current_message)

message_to_print = ['hi', 'hello', 'how are you']
printed_message = []

display_message(message_to_print[:],printed_message)

print(message_to_print)
print(printed_message)