"""
题目：请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。
Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
"""

x=str(input("请输入第一个字母："))
if x=="m":
    print("Monday")
elif x=="T":
    y = str(input("条件不足以判断，请输入第二个字母："))
    if y=="u":
        print("Tuesday")
    else:
        print("Thursday")
elif x=="w":
    print("Wednesday")
elif x=="f":
    print("Friday")
else:
    y = str(input("条件不足以判断，请输入第二个字母："))
    if y == "a":
        print("Saturday")
    else:
        print("Sunday")











