from quaternion import Quaternion


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
