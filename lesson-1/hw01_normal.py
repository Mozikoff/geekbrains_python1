import math
import random

__author__ = 'Мозиков Евгений Александрович'


# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


def max_digit(number):
    print('The number is: {}'.format(number))
    maximum = str(number)[0]
    for digit in str(number)[1:]:
        if digit > maximum:
            maximum = digit
    print('Here is the max digit: {}'.format(maximum))


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.


def swap_variables():
    a = input('Please enter first value: ')
    b = input('Please enter second value: ')
    print('Here are your variables: a - {}, b - {}'.format(a, b))
    a, b = b, a
    print('Here are swapped variables: a - {}, b - {}'.format(a, b))


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


def square_equation():
    a = int(input('Enter parameter a: '))
    b = int(input('Enter parameter b: '))
    c = int(input('Enter parameter c: '))
    print('Here are the params: a = {}, b = {}, c = {}'.format(a, b, c))
    d = b * b - 4 * a * c
    if d >= 0:
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print('Equation has two solutions: x1 = {:.2f}, x2 = {:.2f}'.format(x1, x2))
        else:
            x = -b / (2 * a)
            print('Equation has one solution: x = {:.2f}'.format(x))
    else:
        print('Equation has no solutions!')


if __name__ == '__main__':
    max_digit(random.randrange(999999999))
    print('-----------------------------------------------')
    swap_variables()
    print('-----------------------------------------------')
    square_equation()
