class Base:
    def __new__(cls, *args, **kwargs):  # wywołanie przed stworzeniem obiektu\
        # cls - LINK DO samej klasy, ktora jest tworzona(czyli cls wskazuje na Base)
        print("Base new called")
        return super().__new__(cls)  # super - link do klasy bazowej, w ktorej jest wywoływany __new__

    # wszystkie klasy dziedziczone od bazowej klasy object

    def __init__(self, name):
        print("Base constructor called")
        self.name = name


b = Base("b1")
print(b)


class Singleton:
    """Pattern Singleton"""

    __instance = None  # link na obiekt klasy

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:  # jezeli instancja klasy nie istnieje - tworzymy obiekt i przekazujemy link
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name

    def method1(self):
        pass
