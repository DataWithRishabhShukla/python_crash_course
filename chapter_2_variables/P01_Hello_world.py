
"""
1. Syntax Highlighintng - Python iterprepter will scan line by line then apply different color coding to the fucntion / variables / text /loops.
2. Python will keep track of latest value of the variables. 
3. Variable names can not start with number . It can't have space in it.
4. Variables are often described as boxes you can store your value in . However programaticlly variables are labels assigned to the values.
5.  
"""

message = 'Hello Python Interpreter !!'
print(message)

message = 'Second Message !!'
print(message)

# Strings Variables 


sample_string  =  'Python sample strigs !!'
sample_string2 = "Pythn Sample strings 2 !!"

name = 'rishabh kumar shukla '
print(name.title())
print(name.upper())
print(name.lower())

f_name = 'rishabh'
l_name = 'shukla'
full_name = f'{f_name} {l_name}'

# Formatte strings 
print(f'Hello , {full_name.title()}')

# use of white-spaces
print(f'\t {name} \n {f_name}')

# Removing white-spaces 
print('\n'+'*'*10 +'\t Removing white-spaces \t ' + '*'*10)
fav_language = ' python '
print(fav_language.rstrip())
print(len(fav_language))
print(len(fav_language.rstrip()))

print(fav_language.lstrip())
print(fav_language.strip())

# Removing pre-fixes
print('\n'+'*'*10 +'\t Removing pre-fixes \t ' + '*'*10)

url = 'https://github.com/DataWithRishabhShukla/'
print(url.removeprefix('https://'))

"""
Strings :
1. A string is series of characters . Anything inside quotes is cosidered strings in python . You can use both [ ' ' or " "].
2. A methon is an action that python can perform on the piece of data. 
3. name.title() -: title is an Action . '.' is telling python interpreter to callaction on name .
4. Each method is followed by set of parathesis because methods genrally requires  additional inforamtion to perform their work. [title()]
5. f-strings : formatted strings 
6. In programming - Whitespace refers to any non printing characters . Such as spaces, tabs , end of line symbols .
7. rstrip() , lstrip() , strip() functions 

"""