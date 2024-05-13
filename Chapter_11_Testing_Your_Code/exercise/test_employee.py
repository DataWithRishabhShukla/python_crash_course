import sys,os
sys.path.insert(0,os.getcwd())
from employee import Employee

def test_give_default_raise():
    """Test function to check default salary"""
    e1 = Employee('rishabh', 'shukla', 30000)
    prev_sal = e1.salary
    e1.give_raise()
    assert prev_sal == (e1.salary - 5000)
