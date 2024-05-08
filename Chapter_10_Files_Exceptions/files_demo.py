""" 
Chapter 10 - Files and Exceptions

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
