from random import randint


class Money:
    def __init__(self, money):
        self.money = money


m1 = Money(100)  # {'money': 100}


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


p1 = Point(100, 200)  # {'x': 100, 'y': 200, 'color': 'black'}
p2 = Point(200, 100, 'red')  # print(p2.__dict__)

lst = [Point(x, x) for x in range(1, 2000, 2)]
lst[1].color = 'yellow'
print(len(lst))
for item in lst[:5]:
    print(item.__dict__)


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Ellipse:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


shapes = [
    (Line, Rectangle, Ellipse)[randint(0, 2)]  # randomowo twqorzymy 217 obiektów z trojki class z radnomowymi wsp.
    (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)) for n in range(217)]
for shape in shapes:
    if isinstance(shape, Line):
        shape.sp = (0, 0)
        shape.ep = (0, 0)

for shape in shapes[:5]:
    print(str(shape), shape.sp, shape.ep, )


class TrianleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        for side in (self.a, self.b, self.c):
            if not (isinstance(side, float) or isinstance(side, int)):
                return 1
        # if all(map(lambda x: type(x) in (float, int), (self.a, self.b, self.c))): return 1
        # zwroci true kiedy każdy jest true

        if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            return 2

        return 3

a, b, c = map(int, input().split())
tr = TrianleChecker(a, b, c)
print(tr.is_triangle())