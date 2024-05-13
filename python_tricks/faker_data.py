from pprint import pprint as pp
import os 

os.system('clear')
#os.system('pip install Faker')

from faker import Faker
fake = Faker()

user ={}
user['first_name'] = fake.first_name() 
user['last_name'] = fake.last_name()
user['address'] = fake.address()
user['phone_number'] = fake.phone_number()
user['email'] = fake.email()

pp(user)
