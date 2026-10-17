class Vector:
    def __init__(self, coords):
        self.coords = list(coords)

    def __repr__(self):
        return f"Vector({self.coords})"

    def __add__(self, other):
        return Vector(a + b for a, b in zip(self.coords, other.coords))

    def __sub__(self, other):
        return Vector(a - b for a, b in zip(self.coords, other.coords))
        
    def __str__(self):
        return f'Vector x={self.x} y={self.y}'

    def __mul__(self, k):
        return Vector(a * k for a in self.coords)

    __rmul__ = __mul__

    def dot(self, other):
        return sum(a * b for a, b in zip(self.coords, other.coords))

v = Vector([1, 2, 3])
w = Vector([4, 5, 6])

print(v + w)
print(w - v)
print(v * 2)
print(2 * v)
print(v.dot(w))
