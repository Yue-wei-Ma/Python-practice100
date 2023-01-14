"""题目：输出指定格式的日期。"""
import time
import datetime
#输出今日日期
today=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(today)
#创建一个日期对象
date1=datetime.date(2023,3,2)
print(date1)
#日期的运算
date2=date1+datetime.timedelta(days=31)
print(date2)






















