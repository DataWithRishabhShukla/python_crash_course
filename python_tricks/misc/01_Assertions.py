"""
You see, the proper use of assertions is to inform developers about
unrecoverable errors in a program. Assertions are not intended to
signal expected error conditions, like a File-Not-Found error, where
a user can take corrective actions or just try again.

Assertions are meant to be internal self-checks for your program. They
work by declaring some conditions as impossible in your code. If one
of these conditions doesn’t hold, that means there’s a bug in the program.

Python’s Assert Syntax:

    - assert_stmt => assert expression1 ["," expression2]
    - expression1 is the condition we test,
    - The optional expression2 is an error message that’s displayed if the assertion fails.
    - At execution time, the Python interpreter transforms each assert statement
      into roughly the following sequence of statements:

    if __debug__:
        if not expression1:
            raise AssertionError(expression2)
    
    Note - Assert only run when debug is enabled . however sometime while optimizing interpreter disables the debug.
    That results in the not running the assert statement. 

    - Neve pass assert with tuple , always true asserts
    - assert(1==2, 'This should Fail')

Key Takeaways
• Python’s assert statement is a debugging aid that tests a condition
as an internal self-check in your program.
• Asserts should only be used to help developers identify bugs.
They’re not a mechanism for handling run-time errors.
• Asserts can be globally disabled with an interpreter setting.
"""
import os 
os.system('clear')

def apply_discount(product, discount):
    price = product['price'] * (1.0 - discount)
    assert 0 <= price <= product['price'],"Price can't be less than ogp."
    return price

shoes = {'name': 'Nike Jordan', 'price': 14900}
print(apply_discount(shoes, 0.25))

print(apply_discount(shoes, 0.2))

#---------------------------------------------------------

# Wrong way to use assert
def delete_product(prod_id, user):
    assert user.is_admin(), "Must be admin"
    assert store.has_product(prod_id), "Unknown product"
    store.get_product(prod_id).delete()

# If interpreter disables the debug anyone can delete the data.

# Right way of deleting product

def delete_product(prod_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin')
    if not store.has_product(prod_id):
        raise ValueError('Unknown product')
    store.get_product(prod_id).delete()

#---------------------------------------------------------
assert(1==2, 'This should Fail')
print("---")

#########################################################
"""
2.2 Complacent Comma Placement
    - Putting the comma(",") at the end of each element in list,dict,set
    - It helps in identifying the diff after changes
    - Bcoz it's hard for git to track change in same line
    - To resolve 
        - make it multiline
        - add comma at the end of each element

Key Takeaways
    • Smart formatting and comma placement can make your list,
    dict, or set constants easier to maintain.
    • Python’s string literal concatenation feature can work to your
    benefit, or introduce hard-to-catch bugs.
"""

import os 
os.system('clear')

names = [
    'rishabh',
    'charu',
    'Adi',
]

print(names)

#########################################################

"""
2.3 Context Managers and the with Statement

"""

with open('hello.txt', 'w') as f:
    f.write('Hello ')

"""
Opening files using the with statement is generally recommended because
it ensures that open file descriptors are closed automatically after
program execution leaves the context of the with statement. Internally,
the above code sample translates to something like this:
"""
f = open('hello.txt', 'w')
try:
    f.write('message')
finally:
    f.close()


