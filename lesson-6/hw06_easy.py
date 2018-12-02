import math


# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать,
# что такой треугольник нельзя создать и сделать exit(1)


class Triangle:
    a, b, c = 0, 0, 0

    def __init__(self, a, b, c):
        self._check_sides(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() * 0.5
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def print(self):
        print(f'a = {self.a}, b = {self.b}, c = {self.c}')

    @staticmethod
    def _check_sides(a, b, c):
        if not ((b - c < a < b + c) and (a - c < b < a + c) and (a - b < c < a + b)):
            print('You entered wrong sides. Can''t construct a triangle.')
            exit(1)


if __name__ == '__main__':
    tri = Triangle(2, 3, 4)
    tri.print()
    print(f'Perimeter: {tri.perimeter()}')
    print(f'Square: {tri.square():.3f}')
