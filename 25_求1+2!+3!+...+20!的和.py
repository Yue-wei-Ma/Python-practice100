"""
求1+2!+3!+...+20!的和
"""
sum=0
n = 1
for i in range(1,21):
    n *=i
    print(n)
    sum += n

print(sum)


