"""
input(prompt) Function:
    - Takes only one parameter prompt 
    - Write clear prompts 
    - Leave a space after prompt 

Using int() for Numerical input 
    - int(input('Please enter your age ?'))
    - 

While Loop:
    - it executes a code block as long as condition is true .

Using a flag .

Using break to exit loop .

continue 
    - continue will move the execution to the start if the loop 
"""

import os 
os.system('clear')

prompt = '\nPlease enter the name of a city that you have visited: '
prompt += "\n(Enter 'quit' when you're finished)"

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f'I would love to go to {message.title()}')


current_number =1 

while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = '\nTell me something , I will repeat it back to you. \n'
prompt += 'Enter quit to exit the program: '
flag = True
while flag:
    message = input(prompt)
    if message == 'quit':
        flag = False
    else:
        print(message)

# message = input("Tell me somthing , I will repeat it back to you: ")
# print(message)


# name = input('Please , Enter your name: ')
# print(f'Hello, {name.title()}')

# age = int(input('Please enter your age: '))
# print(f"You're years {age} old .")

# number = int(input('Enter a number , and I will tell you if odd or even ? '))

# if number % 2 == 0 :
#     print("It's even number. ")
# else :
#     print('It is a odd number.')