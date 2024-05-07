

import os 
os.system('clear')

def make_tshirt(tshirt_size='L' , message='I love Python'):
    """ Function to display size and message of tshirt """
    print(f"T-shirt with size {tshirt_size} has message - {message} printed on it.")


make_tshirt('L','Atlassian crack')
make_tshirt(tshirt_size='XS',message='Atlassian crack')
make_tshirt()

def describe_city(city_name , coutnry):
    """ Function to display country and city details!!"""
    print(f"\n{city_name.title()} is in {coutnry.title()}.")

describe_city('delhi','india')