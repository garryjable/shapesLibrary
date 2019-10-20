import ABS

class Shape(ABS):
    item_id
    tag
    components

    @abstract_method
    def compute_area(self):
        area = 0
        for component in self.components:
            area += component.computeArea()
        return area

        print("computing the area")

    @abstract_method
    def move(self):
        print("moving the shape")

    @abstract_method
    def scale(self):
        print("scaling the shape")

    @abstract_method
    def get_drawable(self):
        drawables = []
        for component in self.components:
            drawables.append(component.get_drawable())
        return drawables 


class CompositeShape(Shape):
    components
    
    def compute_area(self):
        area = 0
        for component in self.components:
            area += component.computeArea()
        return area

        print("computing the area")

    def move(self):
        print("moving the shape")

    def scale(self):
        print("scaling the shape")

    def get_drawable(self):
        drawables = []
        for component in self.components:
            drawables.append(component.get_drawable())
        return drawables 

#class Polygon(Shape):
#    coordsList
#    
#    def compute_area(self):
#        print("shitty linear algebra problem")
#
#    def scale(self):
#        print("even shittier linear algebra problem")
#
#    def move(self):
#        print("somewhat shitty linear algebra problem")
#
#    def get_drawable(self):
#        print("return tkinter obj")


class Rectangle(Shape): # tkinter polygon
    coordsList
    
    def compute_area(self):
        print("shitty linear algebra problem")

    def scale(self):
        print("even shittier linear algebra problem")

    def move(self):
        print("somewhat shitty linear algebra problem")

    def get_drawable(self):
        print("return tkinter obj")

class Triangle(Shape): # tkinter polygon
    coordsList
    
    def compute_area(self):
        print("shitty linear algebra problem")

    def scale(self):
        print("even shittier linear algebra problem")

    def move(self):
        print("somewhat shitty linear algebra problem")

    def get_drawable(self):
        print("return tkinter obj")


class Circle(Shape): # tkinter oval
    coordsList

    def computeArea(self):
        print("return area of oval")

    def scale(self):
        print("make the two coordinates of the bounding rectangle bigger")

    def move(self):
        print("make the two coordinates of the bounding rectangle more different")

    def get_drawable(self):
        print("return tkinter obj")


#class Arc(Shape):
#
#    def computeArea(self):
#        print("no op unless it's a pieslice")
#
#    def scale(self):
#        print("a yeah we big now")
#
#    def move(self):
#        print("we moving now bois")
#
#    def get_drawable(self):
#        print("return tkinter obj")


class Image(Shape):

    def scale(self):
        print("wez a sqar")

    def compute_area(self):
        print("wez a sqar")

    def move(self):
        print("wez a sqar")

    def get_drawable(self):
        print("return tkinter obj")


class Line(Shape):

    def compute_area(self):
        return 0

    def move(self):
        print("translate me")

    def scale(self):
        print("enlengthenify the line")

    def get_drawable(self):
        print("return tkinter obj")

class Point(Shape): # tkinter oval with small radius
    coords

    def compute_area(self):
        return 0

    def move(self):
        print("literally a setter function for coords")

    def scale(self):
        print("noop")

    def get_drawable(self):
        print("return tkinter obj")

