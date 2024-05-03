"""
Functions

import pizza
from pizza import make_pizza
import pizza as pz
from pizza import make_pizza as mp

pizza.make_pizza(30,'corn','cheese','olive')
make_pizza(40,'cheese','tomato')
pz.make_pizza(50,'butter','cheese')
mp(30,'bread','cheese')

Storing yur Functions in Modules :

    - One advantage of functions is the way they seperate blocks of code from your main program.
    - you can go as step further by storing your functions in a seperate file called module and
    then importing that module into your main program .
    - An import statement tells python to make the code in a module available in the currently 
    running prgram file . 
    - storing your functions in a seperate file allows you to hide the detail of your program's 
    code and focus on it's higher level logic .
    - it also allows you to re-use functions in many different programs . when you store you func
    in a seperate file you can share those files with other programers without having to share your
    entire prpgram.

Importing an entire module 
    
    - To start importing function first you need to create a module . A module is .py file that contains
    the code you want to import into your program.
    - Let's make a module that contains the function make_pizza() to make this module we put this function into a pizza.py file .
    - when python reads this file the line import pizza tells tells python to open the file pizza.py and copy all the functions 
    from it into this program.
    - It does that in background. 
    - All you need to know is any functions defined in the pizza.py will be available into your current .py file.
    - To call a function a from the imported module 
        - <module_name>.<function_name>(<argements>)
        - import pizza
        - pizza.make_pizza(30,'corn','cheese','olive')
    
    - This first approach to importing in which you simply write import <module> make every function from the module available in your
    program . If you use this kind of import statement all the func will be available in your program.

Importing Specific functions 

    - You can also import specific function from a module 
        - from <module_name> import <function_name>
        - from pizza import make_pizza
    - you can import as many functin as you want from a module by sperating each func name with ","
        - from <module_name> import <function_name_0> , <function_name_1> ,<function_name_2>
    - With this syntax you don't need to use dot notation when you call a function 

Using as to give a function/ module alias 
    - import pizza as p
    - from pizza import make_pizza as mp

Importing all function in a module 
    - from pizza import *

Styling Functions 
    - Functions should have descriptive names and these names should use lowercase letter and underscore
    - Module names should use these convetions as well
    - Every function should have a comment in doc string format  """ """
    - Comment should appear immediately after the function defnition 
    - If you specify a default for a parameter no space should be used on either side of equal sign 
        def function_name(param_0, param_1='default_value')
    - The same convention should be used for keyword argument in function call 
        function_name(value_0, param_1='value')
    - all import should come at the begining only thing allowed before it is comments
    - If module has more than one function it should have two blank lines between function 
    definitions. 

"""