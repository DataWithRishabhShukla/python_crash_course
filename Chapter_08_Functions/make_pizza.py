import pizza
from pizza import make_pizza
import pizza as pz
from pizza import make_pizza as mp

import os
os.system('clear')

pizza.make_pizza(30,'corn','cheese','olive')
make_pizza(40,'cheese','tomato')
pz.make_pizza(50,'butter','cheese')
mp(30,'bread','cheese')