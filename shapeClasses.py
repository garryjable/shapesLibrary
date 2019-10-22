from abc import ABC, abstractmethod
from tkinter import PhotoImage


class Shape(ABC):
    xCoord = 0
    yCoord = 0
    item_id = ''
    measurements = {}

    def __init__(self, *args, **kwargs):
        self.xCoord = kwargs['xCoord']
        self.yCoord = kwargs['yCoord']
        self.measurements = kwargs['measurements']

    def get_coords(self):
        return (self.xCoord, self.yCoord)

    @abstractmethod
    def compute_area(self, *args, **kwargs):
        return

    def move(self, *args, **kwargs):
        self.xCoord = kwargs['newXCoord'] 
        self.yCoord = kwargs['newYCoord'] 
        print("moving the shape")

    def scale(self, *args, **kwargs):
        new_measurements = self.measurements
        for key, val in self.measurements.items():
            new_measurements[key] = val * kwargs['factor']
        self.measurements = new_measurements

    @abstractmethod
    def get_drawable(self, *args, **kwargs):
        drawables = []
        for component in self.components:
            drawables.append(component.get_drawable())
        return drawables 


class CompositeShape(Shape):
    components =[]
    # item id is a tinkter tag

    def compute_area(self, *args, **kwargs):
        area = 0
        for component in self.components:
            area += component.computeArea()
        return area

        print("computing the area")

    def move(self, *args, **kwargs):
        print("moving the shape")

    def scale(self, *args, **kwargs):
        print("scaling the shape")

    def get_drawable(self):
        drawables = []
        for component in self.components:
            drawables.append(component.get_drawable())
        return drawables 


class Rectangle(Shape): # tkinter polygon

    def compute_area(self, *args, **kwargs):
        return self.measurements['width'] * self.measurements['length']

    def get_drawable(self, *args, **kwargs):
        print("return tkinter obj")


class Triangle(Shape): # tkinter polygon

    def compute_area(self, *args, **kwargs):
        return (4.33) * ( self.measurements['side'] ** 2 )

    def get_drawable(self, *args, **kwargs):
        print("return tkinter obj")


class Circle(Shape): # tkinter oval


    def computeArea(self, *args, **kwargs):
        self.measurements['radius'] *= kwargs['factor']
        return 3.14 * self.measurements['radius'] ** 2

    def move(self, *args, **kwargs):
        print("make the two coordinates of the bounding rectangle more different")

    def get_drawable(self, *args, **kwargs):
        print("return tkinter obj")


class Image(Rectangle):
    filename = ''

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        self.filename = kwargs['filename']


class Line(Shape):
    xCoord2 = 0
    yCoord2 = 0

    def __init__(self, *args, **kwargs):
        super(Line, self).__init__(*args, **kwargs)
        self.xCoord = kwargs['xCoord2']
        self.yCoord = kwargs['yCoord2']

    def compute_area(self, *args, **kwargs):
        return 0

    def move(self, *args, **kwargs):
        super(Line, self).move(*args, **kwargs)
        self.xCoord2 = kwargs['newXCoord2']
        self.yCoord2 = kwargs['newYCoord2']

    def get_coords(self):
        return [(self.xCoord, self.yCoord), (self.xCoord2, self.yCoord2)]


    def get_drawable(self):
        print("return tkinter obj")


class Point(Shape): # tkinter oval with small radius

    def compute_area(self, *args, **kwargs):
        return 0

    def scale(self, *args, **kwargs):
        print("noop")

    def get_drawable(self, *args, **kwargs):
        print("return tkinter obj")
