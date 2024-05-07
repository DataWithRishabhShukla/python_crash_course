

prompt = "\nPlease enter the toppings: \n"
prompt +="(Please enter 'quit' to exit.)"

flag = True
while flag:
    topping = input(prompt)

    if topping == 'quit':
        flag = False
    else :
        print(f'Adding the toppings: {topping}')