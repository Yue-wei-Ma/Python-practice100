"""判断101-200之间有多少个素数，并输出所有素数。"""
import math

#熟练度★★
for i in range(101,201):
    flag=1
    k=int(math.sqrt(i))+1
    for j in range(2,k):
        if i%j==0:
            flag=0
            break
    if flag==1:
        print(i)



