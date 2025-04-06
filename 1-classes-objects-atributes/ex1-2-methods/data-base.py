import sys

#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ["1 Dima 24 3244",
          "2 Kris 24 345646",
          "3 Pasha, 19 4546"]


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        max_lim = (b + 1) if len(self.lst_data) > (b + 1) else len(self.lst_data)
        return self.lst_data[a:max_lim]

    def insert(self, data):
        for string in data:
            self.lst_data.append({ self.FIELDS[i]: string.split()[i] for i in range(len(self.FIELDS)) })


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
#[{'id': '1', 'name': 'Dima', 'old': '24', 'salary': '3244'},
# {'id': '2', 'name': 'Kris', 'old': '24', 'salary': '345646'},
# {'id': '3', 'name': 'Pasha,', 'old': '19', 'salary': '4546'}]