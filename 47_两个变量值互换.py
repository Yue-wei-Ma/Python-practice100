"""
题目：两个变量值互换。
"""
import random


def exchange(a,b):
    a=a^b
    b=a^b
    a=b^a
    return a,b

a,b=random.randrange(100),random.randrange(100)
print(a,b)
print(exchange(a,b))
