"""
Iterators are class based iterartors 
How to write iterators faster and with less code using generators and yield keyword

Writing the iterator class using generator 
Generator looks like regular function but instead od using return statement they use yield to pass data back to caller .

How do generator work :
    - They are like normal function but behaviour is quite different
    - For starter calling a generator function doesn't even run the function. It merely created and returns a generator object.
    - Code in the generator function only ececutes when next() is called 
    - If you read the code of the repeater funcitomn again , it looks like the yield keyword in there somehow stops this generator function executin
        midway then resumes it at a later point in time.
    - Execution can be called anytime using the next function on the generator function 

    ....

Generators That Stops Generating 
    - Gnerator stops executing when control return from it other than yield statement

"""

# def repeater(value):
#     while True:
#         yield value

# generator_obj = repeater('rishabh')
# print(repeater('hey'))
# print(next(generator_obj))


# Generators That Stops Generating 
def repeater_that_Stops(value):
    yield value
    yield value
    yield value

for x in repeater_that_Stops('hello'):
    print(x)

# repeater_with_limit
def repeater_with_limit(value, max_limit):
    count = 0
    while True:
        if count > max_limit :
            return
        count += 1
        yield value

for x in repeater_with_limit('rishahb', 3):
    print(x)

# Another way to implement 
def repeater_with_limit(value, max_limit):
    for i in range(max_limit):
        yield value
    # Default return from each function is None

for x in repeater_with_limit('charu', 2):
    print(x)

import os
os.system('clear')

def test_generator(value):
    yield value

for t in test_generator('tom'):
    print(t)