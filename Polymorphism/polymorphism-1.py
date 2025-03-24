class shape:
    def area(self):
        return "Undefined"
class rectangle(shape):
    def __init__(self,length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
shapes=[rectangle(2,3),circle(5)]
for i in shapes:
    print(i.area())