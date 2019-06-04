#coding=utf-8

from collections import defaultdict, Counter
import json

colours =(
        ('Yasoob', 'green'),
        ('Ali', 'blue'),
        ('Sopheia','red'),
        ('Ali', 'pink'),
        ('Kate', 'white'),
        ('Yasoob', 'yellow')
        )
favoriate_color = defaultdict(list)
for name, color in colours:
    favoriate_color[name].append(color)
print(favoriate_color)

favs = Counter(name for name, color in colours)
print(favs)

tree = lambda: defaultdict(tree)
some_tree = tree()
some_tree['favoriate']['color'] = 'yellow'
print(json.dumps(some_tree))

