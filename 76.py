"""
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""
def sumfr(n):
    ls = [1/i for i in range(n,0,-2)]
    return sum(ls)
n = int(input('input a number:\n'))
print(sumfr(n))
