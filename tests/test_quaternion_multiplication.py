from quaternion import Quaternion


def test_quaternion_multiplication() -> None:
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q1 * q2

    assert result.a == -60
    assert result.b == 12
    assert result.c == 30
    assert result.d == 24


def test_quaternion_multiplication_identity() -> None:
    q = Quaternion(1, 2, 3, 4)
    identity = Quaternion(0, 0, 0, 0)
    result = q * identity

    assert result.a == 0
    assert result.b == 0
    assert result.c == 0
    assert result.d == 0


def test_quaternion_multiplication_three() -> None:
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    q3 = Quaternion(9, 10, 11, 12)

    result = q1 * q2 * q3
    assert result.a == -1278
    assert result.b == -396
    assert result.c == -294
    assert result.d == -672