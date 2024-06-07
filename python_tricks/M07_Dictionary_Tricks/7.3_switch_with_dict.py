"""
Emulating switch or case with dictionary 
    - used to replace if-elif chains 
    - 


"""
"""
if cond == 'cond_a':
    handle_a()
elif cond == 'cond_b':
    handle_b()
else:
    handle_dfault()
"""

func_dict = { 
    'cond_a':'handle_a()',
    'cond_b':'handle_b()'
    }

# cond = input("Please proide the input: ")
print(func_dict.get('cond', 'handle_default()'))
print('\n')
# Another example 
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y 
    elif operator == 'div':
        return x / y

print(dispatch_if('add', 10, 20 ))


# we need to add () at the end otheriwse it will return the address of lambda function 
def dispath_if_with_dict(operator, x, y):
    return {
        'add': lambda : x + y,
        'sub': lambda : x - y,
        'mul': lambda : x * y,
        'div': lambda : x /y 
    }.get(operator, lambda : None)()

print(dispath_if_with_dict('add', 10, 10))