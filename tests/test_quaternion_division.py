from quaternion import Quaternion

def test_quaternion_division() -> None:
    q1 = Quaternion(10, 10, 20, 30)
    q2 = Quaternion(2, 2, 2, 2)
    result = q1 / q2

    assert result.a == 8.75
    assert result.b == -1.25
    assert result.c == 3.75
    assert result.d == 1.25

def test_quaternion_division_by_zero() -> None:
    q1 = Quaternion(10, 10, 20, 30)
    q2 = Quaternion(0, 0, 0, 0)
    result = q1 / q2

    assert result == None



