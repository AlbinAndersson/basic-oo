import pytest
from exercises.oo import Rectangle


def test_rectangle_creation():
    r1 = Rectangle(10, 20)
    assert r1.width == 10
    assert r1.height == 20

    r2 = Rectangle(30, 50)
    assert r2.width == 30
    assert r2.height == 50


def test_rectangle_repr():
    r1 = Rectangle(10, 20)
    assert r1.__repr__() == '<Rectangle: 10, 20>'

    r2 = Rectangle(30, 50)
    assert r2.__repr__() == '<Rectangle: 30, 50>'


def test_rectangle_area():
    r1 = Rectangle(10, 20)
    assert r1.area() == 200

    r2 = Rectangle(40, 30)
    assert r2.area() == 1200


def test_rectangle_perimiter():
    r1 = Rectangle(10, 20)
    assert r1.perimiter() == 60

    r2 = Rectangle(40, 30)
    assert r2.perimiter() == 140


def test_rectangle_comparison():
    r1 = Rectangle(10, 20)
    r2 = Rectangle(40, 80)
    r3 = Rectangle(10, 30)

    assert r1 == r2
    assert not r1 == r3
    assert not r2 == r3
