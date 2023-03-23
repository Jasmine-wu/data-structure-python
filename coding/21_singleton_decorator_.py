from functools import wraps
import time
import threading


# 单例
# 用装饰器实现
def dog_decorator(func):
    _instance = {}

    @wraps(func)
    def decorator(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)
        return _instance[func]

    return decorator


# 装饰器还可以把类传进去。。。。。
@dog_decorator
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        time.sleep(2)


# dog1 = Dog("zhang", 11)
# print(id(dog1))
# dog2 = Dog("Li", 22)
# print(id(dog2))


def create():
    dog = Dog("zhang", 11)
    print(dog)


for i in range(10):
    t = threading.Thread(target=create(), args=[
        i,
    ])
    t.start()
