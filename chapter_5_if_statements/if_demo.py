
"""
    '==' tests the condition in case sensitive manner
    Equality Operator   -> '=='
    Inequality Operator -> '!='

Checking Multiple condition :
    You can se use 'and' and 'or' for combining the conditions .
    if age >18 and region =='usa':
        print('Allow')

in , not in -> To check check existance of valuein list .

Boolean value  -> True or False 

Types of if statements 
    - simple if statement 
        if age > 18 :
            print('You')

    - if else statment 
    - if-elif-else chain ->  Mutilple if statements 
    - if-elif chain -> You can omit else block in the if-elif chain 

    - In the if-elif chain if once codition is true , it will omit the evalution of remaining conditions .
    - If multiple if can be true then better to go with series of muiltple if statement .
"""

import os 
os.system('clear')
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else :
        print(car.title())


# Checking if value exist in the list 


# Simple If statement
age = 19 
if age > 18 :
    print('You are eligible for voting .')

# if else statment 
if age > 18 :
    print('Please vote .')
else :
    print('You need to wait for few years.')

# if-elif-else chain
age =12

if age < 4:
    price = 0
elif age < 20 :
    price = 10
else :
    price = 15

print(f'Price ticket for you is : {price}$')



