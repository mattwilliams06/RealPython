# A complicated web of multiple-inheritance of classes 
# **kwargs in constructors is used to deconflict argument naming 

class Rectangle:
    def __init__(self, length, width, **kwargs):
       self.length = length
       self.width = width
       super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width 

    def what_am_i(self):
        return 'Rectangle'

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

    def what_am_i(self):
        return 'Square'

class Cube(Square):

    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        # super() is a shortcut for super(Cube, self)
        return self.what_am_i() + ' child of ' + super().what_am_i()

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)
    
    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return 'Triangle'

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['length'] = base
        super().__init__(base=base, **kwargs)

    def surface_area(self):
        base_area = super().area()
        triangle_area = Triangle.area(self)
        return 4 * triangle_area + base_area

    def what_am_i(self):
        return 'RightPyramid'