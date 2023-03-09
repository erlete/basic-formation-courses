class Coordinate:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):

        if not isinstance(value, (float, int)):
            raise TypeError(
                "expected type float or int for"
                + f" {self.__class__.__name__}.x but got"
                + f" {type(value).__name__} instead"
            )
        self._x = float(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):

        if not isinstance(value, (float, int)):
            raise TypeError(
                "expected type float or int for"
                + f" {self.__class__.__name__}.y but got"
                + f" {type(value).__name__} instead"
            )
        self._y = float(value)

    def distance_to_origin(self):
        return ((self.x)**2+(self.y)**2)**0.5

    def __add__(self, c):
        if not isinstance(c, Coordinate):
            raise TypeError(
                "expected type Coordinate for"
                + f" {self.__class__.__name__}.c but got"
                + f" {type(c).__name__} instead"
            )
        new_x_add = c.x + self.x
        new_y_add = c.y + self.y
        new_coor = Coordinate(new_x_add, new_y_add)
        return new_coor

    def __sub__(self, c):
        if not isinstance(c, Coordinate):
            raise TypeError(
                "expected type Coordinate for"
                + f" {self.__class__.__name__}.c but got"
                + f" {type(c).__name__} instead"
            )
        new_x_sub = self.x - c.x
        new_y_sub = self.y - c.y
        new_coor = Coordinate(new_x_sub, new_y_sub)
        return new_coor
