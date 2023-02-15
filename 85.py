"""
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
"""
i=int(input("input a number:"))
sum=9
while sum%i!=0:
    sum=sum*10+9
print(sum)