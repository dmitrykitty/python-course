class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print("Playing " + self.filename)


media1 = MediaPlayer()
media1.open("Eye of a tiger")
media2 = MediaPlayer()
media2.open("Californication")

media1.play()
media2.play()


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        res = []
        for num in self.data:
            if self.LIMIT_Y[0] <= num <= self.LIMIT_Y[1]:
                res.append(num)
        print(*res)


graph1 = Graph()
graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph1.draw()

