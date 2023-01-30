"""
题目：求一个3*3矩阵主对角线元素之和。
"""
#熟练度︎★
print("请输入一个矩阵：")
l=[]
for i in range(3):
    print(" ")
    for j in range(3):
        l.append(int(input("")))
x=0
for k in range(3):
    x+=l[k*k]
print(x)
