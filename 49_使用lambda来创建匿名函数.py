"""
题目：使用lambda来创建匿名函数。
"""
maximum=lambda x,y:(x>y)*x+(x<y)*y
minimum=lambda x,y:(x>y)*y+(x<y)*x

if __name__=="__main__":
    a=10
    b=20
    print("the larger one is %d" %maximum(a,b))
    print("the smaller one is %d" %minimum(a,b))




