import pytest
from exercises.oo import Circle
from math import pi

def test_circle_creation():
    c1 = Circle(10)
    assert c1.radius == 10
    assert c1.color == 'red'

    c2 = Circle(20)
    assert c2.radius == 20
    assert c2.color == 'red'

    c3 = Circle(10, color='blue')
    assert c3.radius == 10
    assert c3.color == 'blue'


def test_circle_repr():
    c1 = Circle(10)
    assert c1.__repr__() == '<Circle: 10>'

    c2 = Circle(50)
    assert c2.__repr__() == '<Circle: 50>'



def test_circle_diameter():
    c1 = Circle(10)
    assert c1.diameter() == 20

    c2 = Circle(20, color='crimson')
    assert c2.diameter() == 40



def test_circle_area():
    c1 = Circle(10)
    assert abs(c1.area() - 10*10*pi) < 0.00001  # Close enough!

    c2 = Circle(20, color='brown')
    assert abs(c2.area() - 20*20*pi) < 0.00001  # Close enough!
