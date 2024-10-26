from quaternion import Quaternion

def test_quaternion_inverse() -> None:
    q = Quaternion(1,2,3,4)
    q_inv = q.inverse()
    identity_approx = q * q_inv # Approximately unit quaternion
    assert (
        abs(identity_approx.a - 1) < 1e-6 and
        abs(identity_approx.b) < 1e-6 and
        abs(identity_approx.c) < 1e-6 and
        abs(identity_approx.d) < 1e-6
    )

def test_quaternion_inverse_zero() -> None:
    try:
        q_zero = Quaternion(0, 0, 0, 0)
        q_zero.inverse()
        assert False
    except ZeroDivisionError: # Except expected, test passed
        pass

def test_quaternion_inverse_unit() -> None:
    q = Quaternion(1,0,0,0)
    q_inv = q.inverse()
    assert (
        abs(q_inv.a - q.a) < 1e-6 and
        abs(q_inv.b - q.b) < 1e-6 and
        abs(q_inv.c - q.c) < 1e-6 and
        abs(q_inv.d - q.d) < 1e-6
    )


def test_quaternion_inverse_negative() -> None:
    q_neg = Quaternion(-1, -2, -3, -4)
    q_neg_inv = q_neg.inverse()
    identity_neg_approx = q_neg * q_neg_inv
    assert (
        abs(identity_neg_approx.a - 1) < 1e-6 and
        abs(identity_neg_approx.b) < 1e-6 and
        abs(identity_neg_approx.c) < 1e-6 and
        abs(identity_neg_approx.d) < 1e-6
    )
