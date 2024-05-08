from pathlib import Path

base_path = "/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/"
guest_name = input("Please enter your name: ")

path = Path(base_path+"guests.txt")
path.write_text(guest_name)

# Writing names file with while loop

names = ''
while True:
    print("Please enter q to exit !!")
    name = input("Please enter your Name: ")
    if name == 'q':
        break
    else:
        names += name +"\n"

path = Path(base_path+"guest_names.txt")
path.write_text(names)

