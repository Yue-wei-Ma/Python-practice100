"""题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。"""
from sys import stdout
for i in range(2,1001):
    s=i
    for j in range(1,i):
        if i%j==0:
            s-=j
    if s==0:
        print(j)









