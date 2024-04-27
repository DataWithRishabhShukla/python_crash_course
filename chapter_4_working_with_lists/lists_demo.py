"""
Iterating List :
    Using for loop 

Looping is imporatant because it's one of the most common ways a compoter automates repetetive tasks.

Indendetion will decide , how code blocks will be clubbed together . 

"""

import os 
os.system('clear')
magicians = ['alice', 'david', 'carolina']

for magician in magicians :
    print(f'Hello {magician.title()} , that was a neat trick')
    print(f"I can't wait to see your next trick {magician.title()} \n " )

print(f'{"*"*60}\n')
for magician in magicians :
    print(f'Hello {magician.title()} , that was a neat trick')
print(f"I can't wait to see your next trick {magician.title()} \n " )

print(f'{"*"*60}\n')
#   Unintended Indent 
message = 'hello student'
print(message)
# Results in error - IndentationError: unexpected indent

print(f'\nEnd of program !!! \n')