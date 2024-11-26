from math import pi

class BaseShape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2

#here the BaseShape class is defined and tested for rectangle and circle shape types  and if we want to add new shape type like Square .. 
# then we have to modify the __init__ and calcualteArea fn  that means we are open for modifications which violates the OCP princple


# Below code shows the OCP princple

from  abc import ABC,abstractmethod

class BaseShape(ABC):
    def __init__(self, shape_type):
        self.shape_type=shape_type
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(BaseShape):
    def __init(self,radius):
        super().__init("Circle")
        self.radius=radius
    def calculate_area(self):
        return pi*self.radius**2

class Rectangle(BaseShape):
    def __init(self,width,height):
        super().__init("rectangle")
        self.width=width
        self.height=height
    def calculate_area(self):
        return self.width*self.height

#Now  there is already Circle ,Rectangle shape exists  and if we want to add Square shape , we are not modifying any logic that is releated to Circle or Rectangle
#  and we are able to create a new shape by extending the baseshape

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2