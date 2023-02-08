"""
题目：输入数组，最大的与第一个元素交换，
最小的与最后一个元素交换，输出数组。
l=[4,121,52,12,4,11,4,55,12,1,54,22,25]
"""
l=[4,121,52,12,4,11,4,55,12,1,54,22,25]
print(l)
max,min=max(l),min(l)
print("max=",max,"min",min)
l.remove(max)
l.remove(min)
l.insert(0,max)
l.append(min)
print(l)

