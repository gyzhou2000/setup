from .ext._ext import c_add

def add(a, b):
    # print("add")
    return c_add(a, b)


def lalala(string):
    print("+++++++++"+string)