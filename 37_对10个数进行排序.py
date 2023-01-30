"""
题目：对10个数进行排序。
"""
#熟练度︎★
print("请输入10个整数：")
l=[]
for i in range(10):
    x = int(input("请输入一个整数:"))
    l.append(x)
for i in range(9):
    for j in range(i+1,10):
        if l[j]<l[i]:
            temp=l[j]
            l[j]=l[i]
            l[i]=temp

print(l)