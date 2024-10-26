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
        pass

    def inverse(self):
        pass

    def __truediv__(self, other):
        pass

    def conjugate(self):
        pass

    def norm(self):
        pass
