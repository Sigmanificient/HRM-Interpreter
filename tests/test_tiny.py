import pytest
from hrm.tiny import Tiny


def test_tiny_operations():
    t: Tiny = Tiny(1)

    assert (t + t) == Tiny(2)
    assert (t - t) == Tiny(0)

    assert (t.increment()) == Tiny(2)
    assert (t.decrement()) == Tiny(1)


def test_tiny_boundaries():
    zero = Tiny(0)
    half = Tiny(Tiny.LIMIT_SIZE // 2 + 1)
    max_ = Tiny(Tiny.LIMIT_SIZE)
    min_ = zero - max_

    assert pytest.raises(ValueError, max_.increment)
    assert pytest.raises(ValueError, min_.decrement)

    with pytest.raises(ValueError):
        _ = zero - half - half

    with pytest.raises(ValueError):
        _ = half + half

    with pytest.raises(ValueError):
        Tiny(Tiny.LIMIT_SIZE + 1)

    with pytest.raises(ValueError):
        Tiny(-Tiny.LIMIT_SIZE - 1)
