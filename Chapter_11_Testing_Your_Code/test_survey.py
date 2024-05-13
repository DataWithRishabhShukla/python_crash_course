import sys
sys.path.insert(0,'/Users/rishabhshukla/git_projects/python_crash_course/Chapter_11_Testing_Your_Code/')
from survey import AnonymousSurvey

def test_single_response():
    """ a function to test the single response"""
    test_survery = AnonymousSurvey("What is the language that learned first to speak ?")
    test_survery.store_response('english')
    assert 'english' in test_survery.responses

def test_muitiple_response():
    """Function to test multiple responses."""
    test_survey1 = AnonymousSurvey("What is the language that learned first to speak ?")
    languages = ['english', 'hindi', 'sanskrit']

    #Storing  the responses
    for language in languages:
        test_survey1.store_response(language)

    #Testing if language exist in the responses
    for language in languages:
        assert language in test_survey1.responses

