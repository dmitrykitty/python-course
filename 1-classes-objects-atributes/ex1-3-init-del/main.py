class Point:
    color = 'red'

    def __init__(self, x=0, y=0):  # konstruktor domyslny
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def __del__(self):
        print("dstr for " + str(self)) #zwykły destruktor - samodzielnie jest wywoływany

#garbage collector - sprawdza, jak na obiekt nie ma żadnej zewnętrznej referencji - można go usuwac
# i przed tym usunięciem wywoływany __del__(self)
pt = Point()
pt0 = Point()
pt1 = Point(2)
pt2 = Point(2, 3)
pt.set_coords(1, 2)
pt3 = Point(y=4)
print(pt.__dict__)  # {'x': 1, 'y': 2}
print(pt0.__dict__)  # {'x': 0, 'y': 0}
print(pt1.__dict__)  # {'x': 2, 'y': 0}
print(pt2.__dict__)  # {'x': 2, 'y': 3}
print(pt3.get_coords())  # (0, 4)
