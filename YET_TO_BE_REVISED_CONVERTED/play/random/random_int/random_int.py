
from random import randint


def my_ri(a, b=None):
    if not b:
        b = a
        a = 0
    return int(random(a, b+1))


for i in range(10):
    print("randomint: {}".format(randint(0, 3)))
    print("my random int: {}".format(my_ri(3)))
