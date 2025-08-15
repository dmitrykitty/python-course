class Loader:
    def parce_format(self, string, factory):
        seq = factory.build_sequence()
        for substring in string.split(","):
            seq.append(factory.build_number(substring))

        return seq


class Factory:
    @staticmethod
    def build_sequence(self):
        return []
    @staticmethod
    def build_number(self, string):
        return float(string)

ld = Loader()
res = ld.parce_format("1.25,2.3,3.56,4.346", Factory())
print(res)