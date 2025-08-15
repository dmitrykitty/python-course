class Translator:

    def add(self, eng, rus):
        if not hasattr(self, 'dictionary'):
            self.dictionary = {}
        if eng in self.dictionary.keys():
            self.dictionary[eng].append(rus)
        else:
            self.dictionary[eng] = [rus]

    def remove(self, eng):
        if eng in self.dictionary.keys():
            del self.dictionary[eng]

    def translate(self, eng):
        if eng in self.dictionary.keys():
            return self.dictionary[eng]
        return None

    def show_all(self):
        for word in self.dictionary.keys():
            print(f"{word}: {", ".join(self.dictionary[word])}")


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "авто")
tr.add("car", "машина")
tr.add("leaf", "лист")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")

tr.show_all()

print(*tr.translate("go"))
tr.remove("leaf")
tr.show_all()
