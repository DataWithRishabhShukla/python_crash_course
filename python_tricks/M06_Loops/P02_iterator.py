# Beautiful iterator - A class that supports dunder __iter__ and __next__ can be iterated with for-in loops 

import os
os.system('clear')

class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return RepeaterIterator(self)
    

repeater = Repeater('hello')

# for item in repeater:
#     print(item)

# Manually emulating the for-in loop

name = Repeater('rishabh')
iterrator = name.__iter__()
print(next(iterrator))

import os 
os.system('clear')

# Bounded Repeater class
class BoundedRepeater:
    def __init__(self, value, max_repeater):
        self.value = value
        self.max_repeater = max_repeater
        self.count = 0

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count > self.max_repeater:
            raise StopIteration
        self.count += 1
        return self.value

b_iter = BoundedRepeater('rishabh', 2)
iterator = iter(b_iter)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

# for x in b_iter:
#     print(x)


# Checking how iter works on the list
lst = [1, 2, 3]
lst_iter = iter(lst)

print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))