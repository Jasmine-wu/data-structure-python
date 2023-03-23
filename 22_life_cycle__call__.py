import time
import threading


class Counter:
    #  对象创建时调用
    # def __new__(cls, *args, **kwargs):
    #     pass

    # 对象初始化时调用
    # 必须加func参数
    def __init__(self, func):
        self.func = func
        # 记录调用次数
        self.count = 0

    # 实现了这个函数，实例会变得可调用callable(dog)=True，没实现，为false
    # 类可以记录数据，可以利用这个特性，实现类装饰器，记录函数被调用的次数
    def __call__(self, *args, **kwargs):
        self.count += 1
        # return self.func(*args, **kwargs)

    # 对象销毁时调用
    def __del__(self):
        print("del call")


@Counter
def call_func():
    print("call_func")


for i in range(10):
    call_func()

print(call_func.count)
