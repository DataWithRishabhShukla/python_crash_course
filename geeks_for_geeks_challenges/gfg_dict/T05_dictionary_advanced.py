#Advance Dictionary Programs

#Python – Create Nested Dictionary using given List
"""
Input : 
    test_dict = {'Gfg' : 4, 'best' : 9}, 
    test_list = [8, 2] 
    Output : {8: {'Gfg': 4}, 2: {'best': 9}} 
"""

import os 
os.system('clear')

test_dict = {'Gfg' : 4, 'best' : 9}
test_list = [8, 2]


zip_tuple = zip(test_list,test_dict.items())
print(zip_tuple)

final_dict = { k:v for k,v in zip_tuple }
print(final_dict)