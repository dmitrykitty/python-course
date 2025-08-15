class MediaPlayer:

    def open(self, file):
            self.filename = file

    def play(self):
        print("Playing " + self.filename)


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("Eye of a tiger")
media2.open("Californication")

media1.play()
media2.play()