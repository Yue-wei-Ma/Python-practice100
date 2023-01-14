"""题目：一球从100米高度自由落下，
每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"""


ball_hight=100
sum=100
for i in range(9):
    ball_hight/=2
    sum+=(ball_hight*2)
print(sum)
ball_hight /= 2
print(ball_hight)

