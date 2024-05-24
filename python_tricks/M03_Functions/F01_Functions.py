import os 
os.system('clear')

def yell(text):
    return text.upper() + '!'

print(yell('hello'))

# Functions are objects.

bark = yell
print(bark('Hello'))

# you can delete earlier defined function and still use it.
# bcoz function and their name two seperate concern

del yell
print(bark('rishabh'))

# Pythn attaches a string idntifier to every function at creation time 
# You can access is using __name__ attribute 
print(bark.__name__)

# You can store function in data structure 
funcs = [bark, str.lower, str.upper]
print('\n\n')
print(funcs)
for f in funcs:
    print(f,f('rishabh shukla')) 