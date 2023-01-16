"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
a=1.0
b=2.0
sum=0.0
for i in range(20):
    sum+=(b/a)
    b=a+b
    a=b-a
print(b,'/',a,'sum=',sum)




b=1
a=2
sum=0
for i in range(0,20):
    x=a/b
    sum+=x
    a=a+b
    b=a-b



print(sum)