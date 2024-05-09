
import os,json
from pathlib import Path

os.system('clear')

def get_stored_username(path):
    """ get stored usernmae id stored."""
    if path.exists():
        content = path.read_text()
        user_name = json.loads(content)
        
        return user_name
    else:
        return None

def get_new_username(path):
    """Takes and stores the user data."""
    user_name = input("Please enter your username:")
    content = json.dumps(user_name)
    path.write_text(content)
    return user_name

def greet_user():
    """Simple function to greet the user."""
    
    base_path = "/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/"
    file_name = base_path+'user_name.json'
    
    path = Path(file_name)
    user_name = get_stored_username(path)
    
    if user_name:
        print(f"Welcome back, {user_name}")
    else:
        user_name = get_new_username(path)
        print(f"We will remember you next time ,{user_name}")

if __name__ == "__main__":
    greet_user()