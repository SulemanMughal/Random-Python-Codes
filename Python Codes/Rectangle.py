class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width*self.height
