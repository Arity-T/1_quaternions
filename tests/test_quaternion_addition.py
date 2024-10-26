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








