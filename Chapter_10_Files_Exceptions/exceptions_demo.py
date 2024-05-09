
"""
Exceptions:

"""

import os 
os.system('clear')

try:
    print(5/0)
except ZeroDivisionError:
    print('Error Occured: You can not devide by 0.')


# Else block 
import os 
os.system('clear')

print("Give me two number , I'll devide them.")
print("Enter q to exit the program.\n\n")

# while True:
#     a = input("\nEnter the first number: ")
#     if a == 'q':
#         break

#     b = input("Enter the second number: ")
#     if b == 'q':
#         break 
#     try:
#         output = int(a) / int(b)
#     except ZeroDivisionError:
#         print("You can't devide by zero!!")
#     else:
#         print(output)


# Handling file not found exceptions
from pathlib import Path

base_path = base_path = "/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/"
path = Path(base_path+"alice.txt")

try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Error: File {path} does not exist!!")
else:
    words = content.split()
    total_words = len(words)
    print(f"Book alice.txt has {total_words} words.")

# Reading multiple books
from pathlib import Path
def count_words(book_name):
    """ This function tries to count the aproximate words in file."""
    base_path = "/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/"
    path = Path(base_path+book_name)

    try:
        content = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, Book {book_name} doesn't exist.\n")
    else:
        words = content.split()
        print(f"{book_name} has {len(words)} words.\n")


book_names = ['alice.txt', 'no_file.txt', 'multiline.txt']
for book in book_names:
    count_words(book)

#Failing silently
