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

"""

def repeater(value):
    while True:
        yield value

generator_obj = repeater('rishabh')
print(repeater('hey'))
print(next(generator_obj))

