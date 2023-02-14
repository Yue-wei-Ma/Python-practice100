"""
题目：八进制转换为十进制
"""
n=0
p=input("input a octal number: \n")
for i in range(len(p)):
    print(p[i])
    print(ord(p[i]))
    print(ord("0"))

    n=n*8+ord(p[i])-ord('0')
print(n)