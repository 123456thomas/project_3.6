
from fake_useragent import UserAgent

# import random

a = [5,7]
b = a
c = b
a = c

del a
print(c, c is b)
a1 = 5
b1 = a1
c1 = b1
a1 = c1
del a1
print(c1, c1 is b1)