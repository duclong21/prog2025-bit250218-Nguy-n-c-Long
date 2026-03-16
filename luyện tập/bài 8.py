# Bài 8:
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


#thu
v1 = Vector(98, 87)
v2 = Vector(16, -6)
v3 = v1 + v2

print(v1)  # Vector(3, 4)
print(v2)  # Vector(1, -2)
print(v3)  # Vector(4, 2)