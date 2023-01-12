"""暂停一秒输出，并格式化当前时间。"""
import time

#熟练度★★
today=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(today)
time.sleep(3)
print(today)
