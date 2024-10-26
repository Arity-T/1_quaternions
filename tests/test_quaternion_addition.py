from quaternion import Quaternion


def test_quaternion_addition() -> None:
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q1 + q2

    assert result.a == 6
    assert result.b == 8
    assert result.c == 10
    assert result.d == 12


def test_quaternion_addition_identity() -> None:
    q = Quaternion(1, 2, 3, 4)
    identity = Quaternion(0, 0, 0, 0)
    result = q + identity

    assert result.a == 1
    assert result.b == 2
    assert result.c == 3
    assert result.d == 4


def test_quaternion_addition_three() -> None:
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    q3 = Quaternion(9, 10, 11, 12)

    result = q1 + q2 + q3
    assert result.a == 15
    assert result.b == 18
    assert result.c == 21
    assert result.d == 24


def test_quaternion_subtraction() -> None:
    q1 = Quaternion(5, 6, 7, 8)
    q2 = Quaternion(1, 2, 3, 4)
    result = q1 - q2

    assert result.a == 4
    assert result.b == 4
    assert result.c == 4
    assert result.d == 4


def test_quaternion_subtraction_identity() -> None:
    q = Quaternion(1, 2, 3, 4)
    identity = Quaternion(0, 0, 0, 0)
    result = q - identity

    assert result.a == 1
    assert result.b == 2
    assert result.c == 3
    assert result.d == 4


def test_quaternion_subtraction_identity_first() -> None:
    q = Quaternion(1, 2, 3, 4)
    identity = Quaternion(0, 0, 0, 0)
    result = identity - q

    assert result.a == -1
    assert result.b == -2
    assert result.c == -3
    assert result.d == -4


def test_quaternion_subtraction_three() -> None:
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    q3 = Quaternion(9, 10, 11, 12)

    result = q3 - q2 - q1
    assert result.a == 3
    assert result.b == 2
    assert result.c == 1
    assert result.d == 0


def test_quaternion_multiplication() -> None:
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q1 * q2

    assert result.a == 70
    assert result.b == 68
    assert result.c == 62
    assert result.d == 60


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
    assert result.a == 2712
    assert result.b == 2716
    assert result.c == 2744
    assert result.d == 2748


def test_quaternion_conjugate() -> None:
    q1 = Quaternion(1, 2, 3, 4)
    result = q1.conjugate()

    assert result.a == 1
    assert result.b == -2
    assert result.c == -3
    assert result.d == -4
