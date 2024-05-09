
"""
Exceptions:

"""

import os 
os.system('clear')

try:
    print(5/0)
except ZeroDivisionError:
    print('Error Occured: You can not devide by 0.')


# Else block 
import os 
os.system('clear')

print("Give me two number , I'll devide them.")
print("Enter q to exit the program.\n\n")

while True:
    a = input("\nEnter the first number: ")
    if a == 'q':
        break

    b = input("Enter the second number: ")
    if b == 'q':
        break 
    try:
        output = int(a) / int(b)
    except ZeroDivisionError:
        print("You can't devide by zero!!")
    else:
        print(output)
        