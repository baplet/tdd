import pytest
from point import Point

tolerance = 0.0001

def test_distance_between_same_point_is_zero():
    a = Point(2.0, 3.0)
    b = Point(2.0, 3.0)
    assert a.distance(b) == pytest.approx(0, tolerance)