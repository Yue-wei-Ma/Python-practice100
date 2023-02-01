"""
题目：数字比较。
"""
def compare(a,b):
    if a>b:
        print("%d大于%d" %(a,b))
    elif a==b:
        print("%d等于%d" %(a,b))
    else:
        print("%d小于%d" %(a,b))

if __name__=="__main__":
    a=int(input("请输入一个数字："))
    b=int(input("请输入一个数字："))
    compare(a,b)