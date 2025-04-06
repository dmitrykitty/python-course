class Point:
    color = "red"
    circle = 2

    def set_coords(self, x, y):  # self aby metod mozna było używać za pomoca obiektów klasy
        # self to referencja na obiekt
        # ten metod lokalnie do obiektu klasy dodaje atrybuty
        self.x = x
        self.y = y

    def get_coords(self):  # to w sumie też są atrybuty, więc można ich dostać za pomocą getattr
        return self.x, self.y  # tuple with coords


pt2 = Point()
pt2.set_coords(1, 2)
print(pt2.__dict__)  # {'x': 1, 'y': 2}
print(pt2.get_coords())


