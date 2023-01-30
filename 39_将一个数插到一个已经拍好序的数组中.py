"""
题目：有一个已经排好序的数组。
现输入一个数，要求按原来的规律将它插入数组中。
"""
a = [1,4,6,9,13,16,19,28,40,100,0]
n=int(input("请输入一个数："))
end=a[9]
if n>end:
    a[10]=n
else:
    for i in range(10):
        if a[i]>n:
            temp1=a[i]
            a[i]=n
            for j in range(i+1,11):
                temp2=a[j]
                a[j]=temp1
                temp1=temp2
            break
print(a)