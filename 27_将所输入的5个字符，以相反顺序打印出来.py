"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""
s=str(input("请输入5个字符："))
i=len(s)
def output(s,i):
    if i==0:
        return
    print(s[i-1])
    output(s,i-1)

output(s,i)