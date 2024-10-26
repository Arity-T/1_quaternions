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
        divisor = other.a ** 2 + other.b ** 2 + other.c ** 2 + other.d ** 2
        try:
            return Quaternion(
                (self.a * other.a + self.b * other.b + self.c * other.c + self.d * other.d) /
                divisor,
                (other.a * self.b - other.b * self.a - other.c * self.d + other.d * self.c) /
                divisor,
                (other.a * self.c + other.b * self.d - other.c * self.a - other.d * self.b) /
                divisor,
                (other.a * self.d - other.b * self.c + other.c * self.b - other.d * self.a) /
                divisor
            )
        except ZeroDivisionError:
            raise ZeroDivisionError("Quaternion divisor of zero")


    def inverse(self):
        norm_squred = self.norm() ** 2
        if norm_squred == 0:
            raise ZeroDivisionError("Cannot invert a zero-norm quaternion")
        conjugate_q = self.conjugate()
        return Quaternion(
            conjugate_q.a / norm_squred,
            conjugate_q.b / norm_squred,
            conjugate_q.c / norm_squred,
            conjugate_q.d / norm_squred
        )

    def norm(self):
        return (self.a**2 + self.b**2 + self.c**2 + self.d**2) ** 0.5
