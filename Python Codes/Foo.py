class Foo:
    def x(self):
        return 5

    def _x_(self):
        return self.__x()

    def __x__(self):
        return 7

    def __x(self):
        return 8

    
