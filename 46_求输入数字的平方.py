"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
"""
import math
while True:
    x=int(input("请输入数字："))
    print("这个数的平方是：%d" %(x**2))
    if x**2<50:
        quit()
    else:
        print("请继续输入")