class ColourRange:
    def __init__(self, lower, upper):

        self._lower = lower
        self._upper = upper

    @property
    def lower(self):
        return self._lower

    @property
    def upper(self):
        return self._upper


BLUE = ColourRange((100, 150, 0), (140, 255, 255))
YELLOW = ColourRange((20, 100, 100), (30, 255, 255))
RED = ColourRange((168, 131, 200), (188, 151, 24))
BLACK = ColourRange((0, 0, 0), (180, 255, 30))
WHITE = ColourRange((0, 0, 200), (180, 255, 255))
GREEN = ColourRange((89, 255, 255), (36, 50, 70))
PURPLE = ColourRange((158, 255, 255), (129, 50, 70))
ORANGE = ColourRange((24, 255, 255), (10, 50, 70))
