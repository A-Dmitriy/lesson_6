class Road:

    count = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5


    def mass (self):
        mass = self._length * self._width * self._width * self._length / 1000
        print(f"Необходимая масса асфальта: {(mass)} т")

r = Road(1000, 5)
r.mass()