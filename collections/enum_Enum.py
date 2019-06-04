#coding = utf-8
from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvard = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8

    kitten = 1
    puppy = 2

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='Perry', age=15, type= Species.cat)
dragon= Animal(name='Dragon', age=31, type= Species.dragon)
tom = Animal(name='Tom', age=21, type= Species.cat)
mity = Animal(name='Mity', age=2, type= Species.kitten)
print(perry.type == mity.type)
print(dragon.type)

#S = Species()
#print(S[1])
#print(S['cat'])
#print(S.cat)

