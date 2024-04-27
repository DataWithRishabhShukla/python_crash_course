"""
tuple 
    Immutable list are called tuple .
    Values of the tuples cann't be changed .
    defining is same as list just use () instead of [].
"""

import os 
os.system('clear')

nums = (1,2,3,4)
print(type(nums))
print(nums)
print(nums[0])

nums[0]=10
print(nums)