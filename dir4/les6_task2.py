class Road():
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def my_func(self):
        m = 25
        t = 5
        my_f = self._length * self._width * m * t
        print(my_f)


my_road = Road(9, 9)

my_road.my_func()
