def make_pizza(size, *toppings):
    """ Printing the list of things that have been requested."""
    print('\n\n')
    print(type(toppings))
    print(f"Making a pizza of {size}-inch with following toppings:")
    for topping in toppings:
        print(f"- {topping}")