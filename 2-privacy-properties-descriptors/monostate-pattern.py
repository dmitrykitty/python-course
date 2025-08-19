class Monostate:
    __shared_attrs = {
        'name': 'John',
        'id': '1234567890'
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


obj1 = Monostate()
obj2 = Monostate() #każdy z obiektow ma wspolne atrybuty name i id. zmiana w jednym powoduje zmiane w innych
#jezeli dodac nowy attr - będzie dodany we wszystkich
obj1.surname = 'Doe' #obj1.__dict['surname'] = 'Doe' - dlatego będzie dodany u wszystkich obiektow klasy
