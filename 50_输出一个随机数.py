"""
题目：输出一个随机数。
"""
#输入0-1之间的随机数
#输入10-20之间的随机数
#输入10-20之间的随机整数

import random
#输入0-1之间的随机数
print(random.random())
#输入10-20之间的随机数
print(random.uniform(10,20))
#输入10-20之间的随机整数
print(random.randint(10,20))