import sys
sys.path.insert(0,"/Users/rishabhshukla/git_projects/python_crash_course/Chapter_11_Testing_Your_Code/")

from name_function import get_formatted_name

# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

def test_first_last_name():
    """Function to test the get_formatted_name """

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
    # print(formatted_name)

# test_first_last_name()