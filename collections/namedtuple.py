#coding=utf-8
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
Penny = Animal(name='Penny', age=5, type='panda')
print(Penny)
print('{} {} {}'.format(Penny.name, Penny.age,Penny.type))
print(Penny[0])

Penny_dict = Penny._asdict()
print(Penny_dict)
print(type(Penny_dict))
for item in Penny_dict:
    print('{}:{}'.format(item, Penny_dict[item]))
