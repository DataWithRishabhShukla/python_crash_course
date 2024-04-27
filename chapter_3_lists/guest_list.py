
def print_guest(guests:list)->None:
    for guest in guests :
        print(f'Welcome to the party {guest.title()}')


guests = ['rishabh','anurag','vaisnavi']
print_guest(guests)

not_coming ='anurag'
guests.remove(not_coming)
print(guests)

new_guest ='kartheek'
guests.append(new_guest)
print(guests)

guests.insert(0,'charu')
guests.insert(2,'harshit')
guests.append('ayush')
print(guests)

print('We have  space for only two guests.')
while len(guests)>2:
    removed_guest = guests.pop()
    print(f'you’re sorry you can’t invite {removed_guest} to dinner')

print(f'final guest are : {guests}')
del guests[1]
del guests[0]
print(guests)