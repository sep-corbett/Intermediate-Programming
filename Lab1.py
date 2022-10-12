# Need newer python
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

class Triangle:
    "This is a triangle class"
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

t1 = Triangle(1, 2, 3)
print(t1.calculate_perimeter())
print(t1.__doc__)
