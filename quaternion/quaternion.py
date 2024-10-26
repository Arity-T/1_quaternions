__all__ = ["Quaternion"]


class Quaternion:
    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self) -> str:
        return f"Quaternion({self.a}, {self.b}, {self.c}, {self.d})"

    def __add__(self, other):
        return Quaternion(
            self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d
        )

    def __sub__(self, other):
        return Quaternion(
            self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d
        )

    def __mul__(self, other):
        return Quaternion(
            self.a * other.a + self.b * other.b + self.c * other.c + self.d * other.d,
            self.a * other.b + self.b * other.a + self.c * other.d + self.d * other.c,
            self.a * other.c + self.b * other.d + self.c * other.a + self.d * other.b,
            self.a * other.d + self.b * other.c + self.c * other.b + self.d * other.a
        )

    def conjugate(self):
        return Quaternion(
            self.a, -self.b, -self.c, -self.d
        )

    def __truediv__(self, other):
        try:
            return Quaternion(
                (self.a * other.a + self.b * other.b + self.c * other.c + self.d * other.d) /
                (other.a ** 2 + other.d ** 2 + other.c ** 2 + other.b ** 2),
                (other.a * self.b - other.b * self.a - other.c * self.d + other.d * self.c) /
                (other.a ** 2 + other.d ** 2 + other.c ** 2 + other.b ** 2),
                (other.a * self.c + other.b * self.d - other.c * self.a - other.d * self.b) /
                (other.a ** 2 + other.d ** 2 + other.c ** 2 + other.b ** 2),
                (other.a * self.d - other.b * self.c + other.c * self.b - other.d * self.a) /
                (other.a ** 2 + other.d ** 2 + other.c ** 2 + other.b ** 2)
            )
        except ZeroDivisionError:
            print("Quanterion divisor of zero")


    def inverse(self):
        pass

    def norm(self):
        pass
