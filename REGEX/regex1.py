import re

text = "The rain in Spain"
#kwadratowe nawiasy dla grupy symboli, z ktorych kazdy pasuje do wyszukiwania [Rr] lub [0123456789]
#mozna wskazywaqc przedział [0-9] lub [a-zA-Z], a dla -5 trzeba wskazac [-0-9]

#inwersja wyszukiwania, np wszystko oprocz liczb [^0-9]

#kwantyfikatory r"[0-9]{2,4}" - liczby od 0 do 9 od 2 do 4 znakow - taki kwantyfikator szuka największą mozliwą długość
#żebgy szukał najmniejszą r"/d{2-4}?" - taki kwantyfikator szuka najmniejszą mozliwą długość
#{m} - dokładnie m razy, {m,}-m i więcej razy, {,m} - nie więcej niz m razy
match = re.search(r"[Sr]ain", text)
print(match)