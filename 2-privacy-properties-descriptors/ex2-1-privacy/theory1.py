from accessify import private, protected

class Point:
    def __init__(self, x, y, z):
        self.x = x  # public
        self._y = y  # protected (umownie protected, dalej jest dostepny od zewnątrz)
        self.__z = z  # private

    def set_coords(self, x, y, z):
        if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
            self.x = x
            self._y = y
            self.__z = z
        else:
            raise ValueError("Invalid coordinates")

    def get_coords(self):
        return self.x, self._y, self.__z

    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


pt = Point(1, 2, 3)
print(pt.x)  # ok
print(pt._y)  # ostrzeżenie
#print(pt.__z)  # error
print(pt._Point__z)
