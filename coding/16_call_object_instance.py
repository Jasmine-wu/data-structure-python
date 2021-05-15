class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, *args, **kwargs):
        print("call A")


if __name__ == '__main__':

    a1=A(10,20)
    a1.myprint()

    #  怎么让这行代码跑起来，即对象实例被调用起来
    a1(80)