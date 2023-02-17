"""
import time
"""
import time

start=time.perf_counter()
for i in range(10000):
    print(i)
end=time.perf_counter()
print("different is %6.3f" %(end-start))
