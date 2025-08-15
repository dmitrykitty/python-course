class AbstactClass:
    def __new__(cls, *args, **kwargs):
        return "Error: No instances for abstract class!"


a = AbstactClass()
print(a)


class SingletonFive:
    __instance = None
    counter = 0
    def __new__(cls, *args, **kwargs):
        if cls.counter < 5:
            cls.counter += 1
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init(self, name):
        self.name = name

    def __del__(self):
        print("SingletonFive deleted")
        SingletonFive.counter -= 1

objs = [SingletonFive(str(n)) for n in range(10)]
for obj in objs:
    print(obj.name)
