"""
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
"""
import time
import random

play_it=input("do you want to play it.(\'y\' or \'n\'")
while play_it=="y":
    c=input("input a character:\n")
    i=random.randint(0,2*32)%100
    print("please input number you guess:\n")
    start=time.perf_counter()
    a=time.time()
    guess=int(input("input your guess:\n"))
    while guess!=i:
        if guess>i:
            print("please input a little smaller")
            guess=int(input("input your guess:\n"))
        else:
            print("please input a little bigger")
            guess=int(input("input your guess:\n"))
    end=time.perf_counter()
    b=time.time()
    var=(end-start)/18.2
    print(var)
    if var<15:
        print("you are very smart!")
    elif var<25:
        print("you are very normal!")
    else:
        print("you are very stupid!")
    print("Congradulations!!")
    print("the number you guess is %d" %i)
    play_it=input("do you want yo play it")


