"""
输入3个数a,b,c，按大小顺序输出。
a.append(input("请输入一个数字："))
"""
lt=[]
for i in range(3):
    lt.append(input("请输入一个数字："))
lt.sort()
print(lt)