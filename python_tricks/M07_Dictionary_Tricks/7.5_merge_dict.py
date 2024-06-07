"""
Ways to merge dictionaries :
    - 
    - last update wins 

    - {**xs, **ys,**os}
    - dict(xs, **ys)
    - xs.update(ys)



"""
import os 
os.system('clear')

xs = {'a': 1 , 'b': 2}
ys = {'b': 3 , 'c': 4}
xs.update(ys)
print(xs)


# Internal representation
def update(dict1, dict2):
    for key, value in dict2.item():
        dict1[key] = value

# Chaining more than one dictionary 
os = {'e':45, 'f':67}
# ks = xs.update(ys).update(os)
# print(ks)


# Another way using dict()
xs = {'a': 1 , 'b': 2}
ys = {'b': 3 , 'c': 4}

ms = dict(xs, **ys)
print(ms)

#using ** operator 
ds = {**xs, **ys,**os}
print(ds)

