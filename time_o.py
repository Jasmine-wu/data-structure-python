# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time

# emum 枚举法 :最笨的方法
start_time = time.time()
for a in range(0,1000):
    for b in range(0, 1000):
        c = 1000 - a - b
        if a + b + c == 1000 and a ^ 2 + b ^ 2 == c ^ 2:
            print("a, b, c :%d, %d ,%d" % (a, b, c))

end_time = time.time()
time = end_time - start_time
print("time is : %d" % (time))

