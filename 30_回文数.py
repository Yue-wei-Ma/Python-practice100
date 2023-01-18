"""
题目：一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同。　
"""

x=input("请输入一个五位数：")
flag=True
for i in range(len(x)//2):
    if x[i]!=x[-i-1]:
        flag=False
        break
if flag:
    print("x是个回文数")
else:
    print("x不是一个回文数")
