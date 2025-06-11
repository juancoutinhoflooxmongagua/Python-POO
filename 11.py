class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x})'
    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x})(y={self.y})'
p1 = Point(1, 2)

print(p1)