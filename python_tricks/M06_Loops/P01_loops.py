

my_item = ['a', 'b', 'c']

x = range(0,10)
print(type(range(1,10)))
print(list(x))


for item in my_item:
    print(item)

for i, item in enumerate(my_item):
    print(i,item)


emails = {
    "rishabh": 'rishabh@gmail.com',
    'charu': 'charu@gmail.com'
}

for name, email in emails.items():
    print(f"{name}  --> {email}")

#List Comprehesnions 

squares = [x * x for x in range(10)]
print(squares)

even_squares = [x * x for x in range(10) if x%2 == 0 ]
print(even_squares)

# Set Comprehensions
set_squares = {x * x for x in range(10)}
print(f"set_squares --> {set_squares}")

# Dict Comprehension
d_squares = {x: x * x for x in range(10)}
print(f"d_squares --> {d_squares}")

#List Slicing
import os
os.system("clear")

# To delete all element of list 
lst = [1, 2, 3, 4, 5]
del lst[:] # Alternative is  lst.clear()
print(lst)

# Slicing to replace all element of the list withoyt creating a new object 
lst[:] = [7, 8, 9]
print(lst)

copied_lst = lst[:]
print(copied_lst is lst)


