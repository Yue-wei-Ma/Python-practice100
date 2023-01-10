"""#一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？"""
import math

#熟练度★★★
i=0
while True:
    if (math.sqrt(i+100)-int(math.sqrt(i+100))==0) and (math.sqrt(i+268)-int(math.sqrt(i+268))==0):
        print(i)
        break
    i += 1
