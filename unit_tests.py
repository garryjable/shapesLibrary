import unittest
from shapeClasses import Shape, CompositeShape, Rectangle, Circle, Line, Point, Image, Triangle


from tkinter import PhotoImage

class ShapeTests():


    def test_compute_area(self):
        area = self.shape.compute_area()
        self.assertEqual(area, self.area)

    def scale_setUp(self):
        self.scale_kwargs = {}
        self.scale_kwargs['factor'] = 2
        self.before = self.shape.compute_area()
        self.shape.scale(**self.scale_kwargs)
        self.after = self.shape.compute_area()

    def test_move(self):
        move_kwargs = {}
        move_kwargs['newXCoord'] = 2
        move_kwargs['newYCoord'] = 2
        self.shape.move(**move_kwargs)
        self.assertEqual(self.shape.get_coords(), (move_kwargs['newXCoord'], move_kwargs['newYCoord']))

    def test_get_drawable(self):
        self.shape.get_drawable()
        print("tested")


class CompositeShapeTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.triangle_init_kwargs = {}
        self.rectangle_init_kwargs = {}
        self.triangle_init_kwargs['xCoord'] = 50
        self.triangle_init_kwargs['yCoord'] = 50
        self.rectangle_init_kwargs['xCoord'] = 50
        self.rectangle_init_kwargs['yCoord'] = 50
        triangle_measurements = {
                'side': 50,
        }
        rectangle_measurements = {
                'width': 50,
                'length': 50
        }
        self.triangle_init_kwargs['measurements'] = triangle_measurements 
        self.rectangle_init_kwargs['measurements'] = rectangle_measurements
        self.side = 50
        self.length = 50
        self.width = 50
        self.tag = "test"
        self.area = (4.33 * triangle_measurements['side'] ** 2) + (rectangle_measurements['width'] * rectangle_measurements['length'])
        triangle  = Triangle(**self.triangle_init_kwargs)
        rectangle = Rectangle(**self.rectangle_init_kwargs)
        self.components = [triangle, rectangle]
        self.shape = CompositeShape(tag=self.tag, components=self.components)


class TriangleTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.init_kwargs = {}
        self.init_kwargs['xCoord'] = 50
        self.init_kwargs['yCoord'] = 50
        measurements = {
                'side': 50,
                }
        self.init_kwargs['measurements'] = measurements
        self.area = 4.33 * measurements['side'] ** 2
        self.shape = Triangle(**self.init_kwargs)

    def test_scale(self):
        self.scale_setUp()
        self.assertEqual(self.before * self.scale_kwargs['factor'] * 2, self.after)

class RectangleTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.init_kwargs = {}
        self.init_kwargs['xCoord'] = 50
        self.init_kwargs['yCoord'] = 50
        measurements = {
                'width': 50,
                'length': 50
                }
        self.init_kwargs['measurements'] = measurements 
        self.area = measurements['width'] * measurements['length']
        self.shape = Rectangle(**self.init_kwargs)

    def test_scale(self):
        self.scale_setUp()
        self.assertEqual(self.before * self.scale_kwargs['factor'] * 2, self.after)

class CircleTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.init_kwargs = {}
        self.init_kwargs['xCoord'] = 50
        self.init_kwargs['yCoord'] = 50
        measurements = {
                "radius": 50,
                }
        self.init_kwargs['measurements'] = measurements
        self.area = 3.14 * measurements['radius'] ** 2
        self.shape = Circle(**self.init_kwargs)

    def test_scale(self):
        self.scale_setUp()
        self.assertEqual(self.before * self.scale_kwargs['factor'] * 2, self.after)


class ImageTests(RectangleTests):

    def setUp(self):
        self.init_kwargs = {}
        self.init_kwargs['xCoord'] = 50
        self.init_kwargs['yCoord'] = 50
        measurements = {
                "width": 50,
                "length": 50
                }
        self.init_kwargs['measurements'] = measurements 
        self.area = measurements['width'] * measurements['length']
        self.init_kwargs['filename'] = "test.png"
        self.shape = Image(**self.init_kwargs)


class LineTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.init_kwargs = {}
        self.init_kwargs['xCoord'] = 50
        self.init_kwargs['yCoord'] = 50
        self.init_kwargs['xCoord2'] = 50
        self.init_kwargs['yCoord2'] = 50
        self.init_kwargs['measurements'] = {} 
        self.area = 0
        self.shape = Line(**self.init_kwargs)

    def test_compute_area(self):
        area = self.shape.compute_area()
        self.assertEqual(0, self.area)

    def test_move(self):
        move_kwargs = {}
        move_kwargs['newXCoord'] = 2
        move_kwargs['newYCoord'] = 2
        move_kwargs['newXCoord2'] = 4
        move_kwargs['newYCoord2'] = 4
        self.shape.move(**move_kwargs)
        self.assertEqual(self.shape.get_coords(), [(move_kwargs['newXCoord'], move_kwargs['newYCoord']), (move_kwargs['newXCoord2'], move_kwargs['newYCoord2'])])

    def test_scale(self):
        self.scale_setUp()
        self.assertEqual(self.before, self.after)
        self.assertEqual(0, self.after)


class PointTests(unittest.TestCase, ShapeTests):

    def setUp(self):
        self.init_kwargs = {}
        self.init_kwargs['xCoord'] = 50
        self.init_kwargs['yCoord'] = 50
        self.init_kwargs['measurements'] = {} 
        self.area = 0
        self.shape = Point(**self.init_kwargs)

    def test_compute_area(self):
        area = self.shape.compute_area()
        self.assertEqual(0, self.area)

    def test_scale(self):
        self.scale_setUp()
        self.assertEqual(self.before, self.after)
        self.assertEqual(0, self.after)



