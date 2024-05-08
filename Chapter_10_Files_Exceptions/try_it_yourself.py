from pathlib import Path
from os import system

system('clear')

path = Path("/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/learning_python.txt")
content = path.read_text()

# Printing the entire content
print(content)

lines = content.splitlines()
data_list =[]

for line in lines:
    data_list.append(line.strip())

#Printing the data after putting in the list
print(data_list[:4])
