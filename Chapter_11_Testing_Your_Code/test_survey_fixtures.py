import pytest
import os, sys
os.system('clear')
print(f"Current working directory: {os.getcwd()}")
sys.path.insert(0,"/Users/rishabhshukla/git_projects/python_crash_course/Chapter_11_Testing_Your_Code")
from survey import AnonymousSurvey

@pytest.fixture

