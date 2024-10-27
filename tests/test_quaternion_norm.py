from quaternion import Quaternion

def test_quaternion_norm() -> None:
    q = Quaternion(1, 2, 3, 4)
    expected_norm = (1**2 + 2**2 + 3**2 + 4**2) ** 0.5
    assert abs(q.norm() - expected_norm) < 1e-6

def test_quaternion_norm_zero() -> None:
    q = Quaternion(0,0,0,0)
    assert q.norm() == 0

def test_quaternion_norm_unit() -> None:
    q = Quaternion(1,0,0,0)
    assert q.norm() == 1

def test_quaternion_norm_negative() -> None:
    q = Quaternion(-1, -2, -3, -4)
    expected_norm = (1**2 + 2**2 + 3**2 + 4**2) ** 0.5
    assert abs(q.norm() - expected_norm) < 1e-6