"""
Generator Expression:

class based iterator >> generators >> generator expression 

Generator Expression:
    - once generator expression is consumed it can't be reused or restarted
    - 

Generator Expression vs List Comprehensions:
    - 

Generator Expression Syntactic sugar :
    - Syntax --> genexpr = (expression for item in collection if condition )

    - is same as below 

    - def generator_expression(expression, collection):
         for item in collection:
             yield expression q

Generator Expression with filtering 
    - iter = ( x*x for x in range(5) if x%2 == 0)

Inline generator expression 
    for item in (x*x in range(4)):
        print(item)


"""
import os 
os.system('clear')

# Syntax : genexpr = (expression for item in collection if condition )
# Generator Expression:
iter = ('hello' for _ in range(2))

for value in iter:
    print(value)


# List comprehensions vs Generator Expression:
listcomp = ['hello' for _ in range(3)]
genexpr = ('hello' for _ in range(3))

print(listcomp)
print(genexpr)

#Generator Expression with filter 
iter = ( x*x for x in range(5) if x%2 == 0)
for v in iter:
    print(v)

#Inline Generator function 
for item in (x*x for x in range(4)):
    print(item) 