""" 
Chapter 10 - Files and Exceptions

Reading a File:
    1. From the module pathlib import class Path 
        a. from pathlib import Path
    2. Define an instance of the class Path
        a. path = Path('<file_path>.txt')
    3. Read the content using the function read_text()
        a. content = path.read_text()
    4. Reads all the  data in form of text .
    5. You can split it in lines using the funcion split_lines()
        a. lines = content.split_lines()
"""

import os
os.system('clear')

from pathlib import Path
path = Path('/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/pi_digits.txt')
content = path.read_text()
print(content)

#Accessing the file lines 
lines = content.splitlines()
for line in lines:
    print(line)

#working with file content
lines = content.splitlines()
pi = ''
for line in lines:
    pi += line.strip()

print(pi)
print(len(pi))

# Pi with million digits
path = Path('/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/pi_million_digits.txt')
content = path.read_text()
lines = content.splitlines()

pi_string = ''
for line in lines:
    pi +=line.lstrip()

print(pi[:66]+"...")
print(len(pi))


# Birthday in pi
from pathlib import Path

path = Path('/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/pi_million_digits.txt')
content = path.read_text()
lines = content.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday: ")

if birthday in pi_string:
    print("Your birtday exist in pi!!")
else:
    print("Your birtday does not exist in pi!!")



# Writing single message to a file 
from pathlib import Path

base_path = "/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/"
path = Path(base_path + "programming.txt")
path.write_text("I love programming.")

# Wiritng multiline message to a file
from pathlib import Path

path = Path(base_path+"multiline.txt")

content = "I love Python.\n"
content += "It has lots of intreseting modules.\n"
content += "Like strings list files exceptions.\n"

print(content)
path.write_text(content)