import pytest
from exercises.oo import Employee


def test_employee_creation():
    e1 = Employee('Charles Babbage', 3000)
    assert e1.name == 'Charles Babbage'
    assert e1.salary == 3000
    assert e1.id == 0

    e2 = Employee('John von Neumann', 4000)
    assert e2.name == 'John von Neumann'
    assert e2.salary == 4000
    assert e2.id == 1

    e3 = Employee('Nikolay Brusentsov', 2000)
    assert e3.name == 'Nikolay Brusentsov'
    assert e3.salary == 2000
    assert e3.id == 2



def test_employee_repr_and_str():
    e1 = Employee('Konrad Zuse', 5000)
    assert e1.__repr__() == '<Employee: Konrad Zuse>'
    assert e1.__str__() == 'Konrad Zuse'

    e2 = Employee('Ada Lovelace', 6000)
    assert e2.__repr__() == '<Employee: Ada Lovelace>'
    assert e2.__str__() == 'Ada Lovelace'


def test_employee_raise_salary():
    e1 = Employee('Joseph Marie Jacquard', 5000)
    assert e1.salary == 5000
    e1.raise_salary(10)
    assert e1.salary == 5500

    e2 = Employee('Alonzo Church', 10000)
    assert e2.salary == 10000
    e2.raise_salary(5)
    assert e2.salary == 10500
    e2.raise_salary(20)
    assert e2.salary == 12600


def test_employee_annual_salary():
    e1 = Employee('James Cooley', 3000)
    assert e1.annual_salary() == 36000

    e2 = Employee('Vannevar Bush', 1000)
    assert e2.annual_salary() == 12000
