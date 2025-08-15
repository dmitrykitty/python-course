class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"Playing video: {self.name}")

class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play_video(cls, index):
        cls.videos[index].play()


v1 = Video()
v1.create("Python. OOP")
v2 = Video()
v2.create("Java")

YouTube.add_video(v1)
YouTube.add_video(v2)

YouTube.play_video(0)
YouTube.play_video(1)