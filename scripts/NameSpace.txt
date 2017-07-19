#from tankist-scratch.github.io/python/scripts/NameSpace.py
#author = tankist-scratch


class NameSpace:
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        return self.__dict__[name]

    def add(self, name):
        self.__dict__[name] = NameSpace()
