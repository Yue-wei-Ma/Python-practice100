"""
题目：列表使用实例。
"""
lt=[1234,"学号",[1,2,3,4,5]]
print(len(lt))
print(lt[1:])
lt.append("i\"m new here!")
print(len(lt))
print(lt[-1])

print(lt.pop(1))
print(len(lt))
print(lt)

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matrix)
print(matrix[1])
col2=[row[1] for row in matrix]
print(col2)
col2even=[row[1] for row in matrix]
print(col2even)