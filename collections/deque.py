#coding=utf-8

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)

print(len(d))

d = deque(range(5))
print(len(d))
print(d)
d.popleft()
d.pop()
print(d)

d.extend([9,7,6])
d.extendleft([0,3,1])
print(d)
