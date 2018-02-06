__author__ = 'jet'
import sys
import os

class Singleton(object):
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

print(hasattr(Singleton, 'test'))
Singleton.test = 1
print(hasattr(Singleton, 'test'))
obj1 = Singleton()
obj2 = Singleton()


def total(a=5, *numbers, **phonebook):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(10)
total(10, 1, 2, 3)
a = (1, 2)

def test(para, func=None):
    print("what we got is {}".format(para))
    print("resutl {}".format(func(para))) if func is not None else None

test(1)
test(2, lambda x: x*x)
a = '123'
b = '12' + '3'
print(a == b)
print(a is b)


p = sys.path
print(os.path)

