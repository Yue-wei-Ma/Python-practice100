"""
题目：求0—7所能组成的奇数个数。
"""
def f(n):
    if n==0:
        return 1
    elif n==1:
        return  7
    else:
        return f(n-1)*8
l=[]
for i in range(1,9):
    l.append(f(i-1)*4)
print(l)
print(sum(l))