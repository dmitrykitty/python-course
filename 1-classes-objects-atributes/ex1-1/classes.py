from xmlrpc.client import MAXINT


class Cat:
    """Description of your class. U can get it by using method Cat.__doc__"""
    name = "Kristinka"
    weight = 5.5
    color = "red"


# obiekty klasy nie przechowywuja atributow dopoki ich nie dodac
a = Cat()
b = Cat()

print(a.name)  # Kristinka
Cat.name = "Dimka"
print(a.name)  # imie zmienie się dla wszystkich obiektow klasa Cat
a.name = "Kristinka"  # teraz w a będzie name Dimka, u reszty Kristinka

Cat.surname = "Nikitina"  # dodanie atrybutu surname
b.surname = "Nikitin"
setattr(Cat, "rating", MAXINT)  # lub w taki sposob
b.rating = 2

print(b.__dict__) #zwraca atrybuty i wartosic: {'surname': 'Nikitin', 'rating': 2}


getattr(b, "rating", False)  # sprawdza czy jest w clasie obiektu b atrybut i jak nie - zwraca false, jak jest - wartosc
# mozna przez class getattr(Cat, "rating", False)
print(type(a))  # sprawdzenie typu <class '__main__.Cat'>
isinstance(a, Cat)  # True

del Cat.weight #usuwamy atrubute, jak nie ma - error
#mozna rownierz usuwac u konkretnego obiekta
del a.weight
#przed usunieciem mozna sprawidzic czy istnieje atrybute
hasattr(Cat, "weight") #Flase, bo juz został usunięty
delattr(Cat, "weight") #mozna usuwac rowniez w taki sposob

a.x, a.y = 1, 2 #tworzenie lokalnych atrybutow dla a - nie ma w klasie
b.z = 6

