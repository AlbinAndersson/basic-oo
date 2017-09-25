from math import pi

class Circle():
    """Implementation av klassen `Circle`.

    Klassen ska ha attributen `radius` och `color`. Attributet `radius` ska
    vara obligatioriskt och attributet `color` ska ha ett standardvärdet `red`.

    Klassen ska ha metoderna `diameter` och `area` som returnerar
    lämpliga värden.

    Implementera den magiska metoden `__repr__` så att ett cirkel-objekt får
    representationen `<Circle: 10>` om den har radien 10.
    """

    def __init__(self, radius, color='red'):
        self.radius = radius
        self.color = color

    def diameter (self):
        return self.radius * 2

    def area (self):
        return self.radius ** 2 * pi

    def __repr__ (self):
        return '<Circle: {}>'.format(self.radius)


class Rectangle():
    """Implementation av klassen `Rectangle`.

    Klassen ska ha attributen `width` och `height`. Båda attributen ska vara
    obligatoriska vid skapandet av objekt.

    Klassen ska ha metoderna `area` och `perimiter` som returnerar
    lämpliga värden.

    Implementera den magiska metoden `__repr__` så att ett rektangel-objekt får
    representationen `<Rectangle: 10, 20>` om den har bredden 10 och höjden 20.

    Implementera även den magisa metoden `__eq__` så att två rectanglar anses
    lika om de har samma proportioner.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__ (self, other):
        return self.width / other.width == self.height / other.height

    def area(self):
        return self.width * self.height

    def perimiter(self):
        return self.width * 2 + self.height * 2

    def __repr__(self):
        return '<Rectangle: {}, {}>' .format(self.width, self.height)



class Employee():
    """Implementation av klassen `Employee`.

    Klassen ska ha attributen `id`, `name` och `salary`. Attributen `name` och
    `salary` ska vara obligatoriska och `id` ska få nästa lediga heltal (med
    start på 0). `id` ska alltså inte anges vid skapandet av nya objekt.

    Klassen ska metoder `raise_salary` med löneökningen angiven som ett
    antal procent.

    Klassen ska även ha en metod `annual_salary` som returnerar den antälldes
    årslön (`salary`-attributet innehåller månadslönen.)

    Metoderna __str__ och __repr__ ska finnas, se testerna för exempel på
    hur deras utdata ska se ut.
    """
    current_id = 0

    def __init__(self, name, salary):
        self.id = Employee.current_id
        Employee.current_id += 1
        self.name = name
        self.salary = salary

    def raise_salary(self, precent):
        self.salary = self.salary * (precent / 100) + self.salary
        return self.salary

    def annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Employee: {}>'.format(self.name)
