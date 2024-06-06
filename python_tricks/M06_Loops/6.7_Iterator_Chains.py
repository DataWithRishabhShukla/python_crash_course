"""
Iterator Chains:


"""


def squared(seq):
    for v in seq:
        yield v*v


def negated(seq):
    for v in seq:
        yield -v


integers = range(8)
print(list(squared(integers)))
print(list(negated(integers)))

print('\n\n')
print(list(negated(squared(integers))))

# Same using generator expression 
print("\n Using the gnerators expression ")
squared_expr = (x*x for x in integers)
negeated_expr = (-x for x in squared_expr)
print(negeated_expr)
print(list(negeated_expr))