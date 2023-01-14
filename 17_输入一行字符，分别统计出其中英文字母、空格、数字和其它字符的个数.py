"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

import string
s=input("请输入字符串：")
letter=0
space=0
digit=0
other=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        other+=1
print('字母有%d个，数字有%d个，空格有%d个,其他有%d个' %(letter,digit,space,other))
