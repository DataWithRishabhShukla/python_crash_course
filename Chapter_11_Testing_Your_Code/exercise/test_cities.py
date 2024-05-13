import sys

sys.path.insert(0, '/Users/rishabhshukla/git_projects/python_crash_course/Chapter_11_Testing_Your_Code/exercise')

from city_functions import get_city_country_names

def test_city_name():
    """Function test the city and country name formatting."""

    formatted_string = get_city_country_names('delhi', 'india')
    assert formatted_string == 'Delhi, India'

def test_city_population():
    """Function tests formatted string the city, country."""

    formatted_String = get_city_country_names('delhi', 'india', 300000)
    assert formatted_String == "Delhi, India - Population 300000"
