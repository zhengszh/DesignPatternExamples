def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

@Singleton
class A(object):
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return str(self.x)

s1 = A(1)
print s1
s2 = A(2)
print id(s1), id(s2)
print s1, s2
