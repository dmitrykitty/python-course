class Vector:
    MIN_COORDS = 0
    MAX_COORDS = 100

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):  # method ktory ma dostep tylko do składowych klasy, ale nie do lokalnych zmiennych
        return cls.MIN_COORDS <= arg <= cls.MAX_COORDS

    @staticmethod
    # method, ktory nie ma dostepu ani do lokalnych, ani do globalnych zmiennych klasy i
    # jest tylko powiązabny z nią
    def norm2(x, y):
        return x ** 2 + y ** 2

v = Vector(10, 150)
print(v.__dict__, Vector.norm2(10, 150))