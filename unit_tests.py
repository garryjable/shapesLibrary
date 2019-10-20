import unittest
from shapeClassess import Shape, CompositeShape, Rectangle, Circle, Line, Point, Image, Triangle

class ShapeTests():

    def test_compute_area(self):
        area = self.shape.compute_area()
        self.assertEqual(area, self.area)

    def test_scale(self):
        factor = 2
        before = self.shape.compute_area()
        self.shape.scale(factor)
        after = self.shape.compute_area()
        self.assertEqual(before ** factor, after)

    def test_move(self):
        newXCoord = 55
        newYCoord = 55
        self.shape.move(55,55)
        self.assertEqual(self.shape.get_coords(), (newXCoord, newYCoord))

    def test_get_drawable(self):
        self.shape.get_drawable()
        print("tested")


class CompositeShapeTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.side = 50
        self.length = 50
        self.width = 50
        self.tag = "test"
        self.area = (4.33 * self.measurement ** 2) + (self.width * self.length)
        triangle  = Triangle(xCoord=self.xCoord, yCoord=self.yCoord, side=self.side)
        rectangle = Rectangle(xCoord=self.xCoord, yCoord=self.yCoord, width=self.width, height=self.height)
        self.components = [triangle, rectangle]
        self.shape = CompositeShape(tag=self.tag, components=self.components)


class TriangleTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.side = 50
        self.area = 4.33 * self.measurement ** 2
        self.shape = Triangle(xCoord=self.xCoord, yCoord=self.yCoord, side=self.side)

class RectangleTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.length = 50
        self.width = 50
        self.area = self.width * self.length
        self.shape = Rectangle(xCoord=self.xCoord, yCoord=self.yCoord, width=self.width, height=self.height)

class CircleTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.radius = 50
        self.area = 3.14 * self.radius ** 2
        self.shape = Circle(xCoord=self.xCoord, yCoord=self.yCoord, radius=self.radius)

class ImageTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.width = 50
        self.height = 50
        self.area = self.width * self.height
        filename = PhotoImage(file = "test.png")
        self.image = Image(xCoord=self.xCoord, yCoord=self.yCoord, width=self.width, height=self.height, image=self.filename)

class PointTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.area = 0
        self.shape = Point(xCoord, yCoord)


class LineTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.xCoord2 = 50
        self.yCoord2 = 50
        self.area = 0
        self.shape = Line(xCoord=self.xCoord, yCoord=self.yCoord, xCoord2=self.xCoord2, yCoord2=self.yCoord2)


class PointTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.xCoord = 50
        self.yCoord = 50
        self.area = 0
        self.point = Point(xCoord=self.xCoord, yCoord=self.yCoord)

