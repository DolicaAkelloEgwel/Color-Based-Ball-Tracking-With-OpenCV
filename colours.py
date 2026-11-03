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