class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, time):
        self.__time = time

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        return type(tm) == int and 0 <= tm <= 100_000
