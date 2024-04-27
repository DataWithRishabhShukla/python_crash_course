"""
Iterating List :
    Using for loop 

Looping is imporatant because it's one of the most common ways a compoter automates repetetive tasks.

Indendetion will decide , how code blocks will be clubbed together . 

The colon at the end of for statement tells Python to interpret the next line as the start of loop. 

range function : 
    range(start_sequence, end_sequence,step_size)
    Defaults : step - 1, start_sequence - 0 
    range(1,5) - 1,2,3,4
    range(6)   - 0,1,2,3,4,5
    numbers = list(range(1,7))

min(digits),max(digits),sum(digits)
    
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

#   Unintended Indent 
print(f'{"*"*60}\n')
message = 'hello student'
print(message)
# Results in error - IndentationError: unexpected indent

# range function 
for num in range(1,5):
    print(num)

print('\n')

for x in range(6):
    print(x)

# using range to make list 
import os 
os.system('clear')
numbers = list(range(1,7))
print(numbers)

squares =[]

for num in range(1,11):
    squares.append(num**2)
print(squares)


digits = list(range(1,11))
print(digits)
print(min(digits),max(digits),sum(digits))


# List comprehensions 
squares = [ val**2 for val in range(1,21)]
print(squares)

t= [x for x in range(1,20)]
print(t)

print(f'\nEnd of program !!! \n')