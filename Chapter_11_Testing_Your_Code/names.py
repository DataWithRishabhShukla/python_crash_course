from name_function import get_formatted_name
import os

os.system('clear')

print("Enter 'q' at any time to quit.\n")
while True:
    first = input("Enter the first name: ")
    if first == 'q':
        break
    last = input("Enter the last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\t Neatly formatted name: {formatted_name}.\n ")