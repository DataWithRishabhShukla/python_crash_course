"""
Base URL : https://www.geeksforgeeks.org/python-set-exercise/

Sets :
    - A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. 

"""
import sys, os


def sets_problem_1():
    """
    Find the size of a Set in Python
    URL : https://www.geeksforgeeks.org/find-the-size-of-a-set-in-python/
    """
    set_1 = {1, "a", "t1", "p1"}
    print(f"Sie of set {set_1}: {sys.getsizeof(set_1)} bytes\n")
    print(dir(set))
    print("\nUsing __sizeof__ \n")
    print(set_1.__sizeof__())

sets_problem_1()
print(sets_problem_1.__doc__)

def sets_problem_2(sample: set):
    """
    Iterate over a set in Python
    URL : https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
    """
    for element in sample:
        print(element)


os.system('clear')
ip_set_1 = {"geeks"}
ip_set_2 = set("geeks")
sets_problem_2(ip_set_1)
sets_problem_2(ip_set_2)


def set_problem_3(sample):
    """Maximum and Minimum in a Set """
    return {"max":max(sample), "min":min(sample)}

input_set = {1,2,3,23,0}
print(set_problem_3(input_set))

def set_problem_3(sample):
    """
    Remove items from Set
        Using the pop() method
            - pop() takes no arguments (1 given)
        Using discard() method
            - input_set.discard(3)
            - does not throw error if element is not present in the set
        Using remove() method
            - input_set.remove(32)
            - throws keyerror if element is not present in the set 
    """
    return {"max":max(sample), "min":min(sample)}

input_set = {1,2,3,4,5}
print(input_set.pop())
print(input_set)
print(input_set.discard(23))
print(input_set)
print(input_set.remove(32))
print(input_set)
print(input_set.pop())