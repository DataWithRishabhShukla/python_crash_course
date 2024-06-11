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



ip_set_1 = {"geeks"}
ip_set_2 = set("geeks")
sets_problem_2(ip_set_1)
sets_problem_2(ip_set_2)


def set_problem_3(sample):
    """ Maximum and Minimum in a Set """
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

input_set = {1,23,32,4,5}
# print(input_set.pop())
# print(input_set)
# print(input_set.discard(23))
# print(input_set)
# print(input_set.remove(32))
# print(input_set)
# print(input_set.pop())



os.system('clear')
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
flag = [True if x in b else False for x in a ]
print(all(flag))

a_set = set(a)
b_Set = set(b)
print(a_set.intersection(b_Set))

from collections import Counter
print(Counter(a))

#Python program to find common elements in three lists using sets
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

ar1_set = set(ar1)
ar2_set = set(ar2)
ar3_set = set(ar3)

print(ar1_set.intersection(ar2_set).intersection(ar3_set))

# Using list comprehension 
print("Using list comprehension ")
print([x for x in ar1 if x in ar2 and x in ar3])


os.system('clear')
#Python | Find missing and additional values in two lists

list1 = [1, 2, 3, 4, 5, 6] 
list2 = [4, 5, 6, 7, 8] 

print(f"Missing elements of list1 form list2 :{set(list1).difference(set(list2))}")
print(f"Common elements of list1 form list2 :{set(list1).intersection(set(list2))}")

#Python | Difference between two lists
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 

print([e for e in list1 if e not in list2 ])
print(set(list1).difference(set(list2)))