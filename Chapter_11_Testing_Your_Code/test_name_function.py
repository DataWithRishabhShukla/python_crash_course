"""
(base) rishabhshukla@Rishabhs-MacBook-Air Chapter_11_Testing_Your_Code % pytest
===================================== test session starts =====================================
platform darwin -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /Users/rishabhshukla/git_projects/python_crash_course/Chapter_11_Testing_Your_Code
plugins: anyio-2.2.0, Faker-25.1.0
collected 1 item                                                                              

test_name_function.py .                                                                 [100%]

====================================== 1 passed in 0.05s ======================================
(base) rishabhshukla@Rishabhs-MacBook-Air Chapter_11_Testing_Your_Code % 

"""

import sys, os

os.system('clear')
# Add the absolute path of the directory containing the module to the Python path
sys.path.insert(0,"/Users/rishabhshukla/git_projects/python_crash_course/Chapter_11_Testing_Your_Code/")

from name_function import get_formatted_name

def test_first_last_name():
    """Function to test the get_formatted_name """

    formatted_name = get_formatted_name('rishabh', 'shukla')
    assert formatted_name == 'Rishabh Shukla'

def test_first_middle_last_name():
    """Function to test the get_formatted_name """

    formatted_name = get_formatted_name('rishabh','shukla' ,'kumar')
    assert formatted_name == 'Rishabh Kumar Shukla'

