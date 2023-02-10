"""
题目：反向输出一个链表。
"""
lt=[]
for i in range(5):
    lt.append(int(input("请输入一个数：\n")))
print(lt)
lt.reverse()
print(lt)