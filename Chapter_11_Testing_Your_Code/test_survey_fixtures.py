import pytest
import os, sys
os.system('clear')
print(f"Current working directory: {os.getcwd()}")
sys.path.insert(0,"/Users/rishabhshukla/git_projects/python_crash_course/Chapter_11_Testing_Your_Code")
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test function."""
    question = "what language did you first learn to speak ?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('english')
    assert 'english' in language_survey.responses

def test_multiple_response(language_survey):
    response = ['english', 'hindi', 'tamil']
    for language in response:
        language_survey.store_response(language)
    
    for language in response:
        assert language in language_survey.responses
