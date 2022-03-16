"""
Random

Random is an inbuilt python module in whoch we can generate random values.

"""
"""


x = random.randint(0, 6)
print(x)

print(dir(random))

y = random.sample([10, 20, 30, 40, 50], k=1)
print(y)


p1 = random.randint(1, 9)

print(p1)

"""
"""

import random
password = ''

for i in range(8):
    password += str(random.randint(0, 9))

print(password)


p = random.randint(5, 8)

temp = random.sample(
    ['a', 'b', 'c', 'A', 'B', 'C', 'D', '1', '2', '3', '4', '*', '%', '#'], k=p)

password = ''

for i in temp:
    password += i
print(password)


"""


def display():
    i = 0
    while i < 10:
        print(" + ", end='')
        i += 1
    print()
    i = 0
    while i < 10:
        print("+                              +")
        i += 1
    i = 0

    while i < 10:
        print(" + ", end='')
        i += 1


display()
