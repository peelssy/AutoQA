class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def acreage(self):
        s = self.a * self.b
        return s

    def perimeter(self):
        p = (self.a + self.b) * 2
        return p

p = Rectangle(4, 5)
print(p.perimeter())
print(p.acreage())

class Distance:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mo(self):
        m = (self.x**2 + self.y**2)**0.5
        return m
    def m1(self, x2, y2):
        d = ((x2 - self.x)**2 + (y2 - self.y)**2)**0.5
        return d

s = Distance(-5, 12)
print(s.mo())

print(s.m1(2,3))