__all__ = ['add']  #all默认作用在*上，不会影响手动导入，all默认为数组，
                   #数组中的函数为当使用from my_mudule1 import *时默认会导入的函数

def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)


if __name__ == '__main__': #当右键运行时if后为真可以运行，当导入时if不为真不能运行
    add(3,5)