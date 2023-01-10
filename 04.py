#输入某年某月某日，判断这一天是这一年的第几天？
#days=[0,31,59,90,120,151,181,212,243,273,304,334,365]
#熟练度★★★★
year=eval(input("请输入年份："))
month=eval(input("请输入月份："))
day=eval(input("请输入日期："))
days=[0,31,59,90,120,151,181,212,243,273,304,334,365]


if (year%4==0 and year%100!=0) or year%400==0:
    if month>2:
        num=days[month-1]+day+1
    else:
        num = days[month - 1] + day
else:
    num = days[month - 1] + day

print(num)







