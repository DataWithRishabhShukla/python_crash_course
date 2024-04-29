
import os 
os.system('clear')

usernames = ['admin','Jaden','rishabh','charu','anurag','neeraj']
usernames =[]

if usernames :
    for user in usernames :
        if user == 'admin':
            print(f'Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')

else :
    print('We need to find some users!')


numbers = list(range(1,10))
print(numbers)

for number in numbers :
    if number == 1 :
        print(f'{number}st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')