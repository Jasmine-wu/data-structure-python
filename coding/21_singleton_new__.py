import time
import threading


class Dog:
    # 对象创建时调用
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    # 对象初始化时调用
    def __init__(self, name, age):
        self.name = name
        self.age = age
        time.sleep(2)

    # 实现了这个函数，实例会变得可调用callable(dog)=True，没实现，为false
    def __call__(self, *args, **kwargs):
        pass

    # 对象销毁时调用
    def __del__(self):
        print("del call")


def create():
    dog = Dog("zhang", 11)
    print(dog)
    print(callable(dog))


for i in range(10):
    t = threading.Thread(target=create(), args=[
        i,
    ])
    t.start()
