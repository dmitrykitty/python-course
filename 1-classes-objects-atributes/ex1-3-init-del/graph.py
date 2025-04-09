class Graph:

    def __init__(self, data):
        self.data = data
        self.is_show = True

    def set_data(self, data):
        self.data = data

    def show(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Private data")

    def graph(self):
        if self.is_show:
            print("Graphic representation of the data: ", *self.data)
        else:
            print("Private data")

    def set_show(self, show):
        self.is_show = show

data_graph = list(map(int, input().split()))
g = Graph(data_graph)
g.graph()
g.set_show(False)
g.show()
