# Mixin: An independent class thay gets pulled in in the inheritance hierarchy, but isn't going
# to affect anything that inherits it

class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area

# All that's required for the SurfaceAreaMixin is that somewhere in the class that's using
# it, there's an attribute called 'surfaces'.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length=length, width=length)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]