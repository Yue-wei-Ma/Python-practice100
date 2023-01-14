"""题目：求s=a+aa+aaa+aaaa+aa...a的值，
其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。"""

a=eval(input("请输入a："))
n=eval(input("请输入你："))
s=0
for i in range(1,n+1):
    for j in range(i):
        a=(n*((10)**j))
        s+=a
print(s)
