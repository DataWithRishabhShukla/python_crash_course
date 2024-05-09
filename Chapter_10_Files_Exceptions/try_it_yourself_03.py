import os 
os.system('clear')

#10-6. Addition:
try:
    num1 = int(input("Enter the first num: "))
    num2 = int(input("Enter the second num: "))
except ValueError:
    print("Please enter only integer!!")
else:
    print(num1+num2)

#10-9. Silent Cats and Dogs:
from pathlib import Path

cats = ['cat.txt', 'billi.txt']
dogs = ['dog.txt', 'kutta.txt', 'alice.txt']

cats.extend(dogs)
base_path = "/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/"

for file_name in cats:
    path = Path(base_path+file_name)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"{file_name} has {content.lower().count('the')} many 'the'.")
