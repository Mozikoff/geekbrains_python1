import random

__author__ = 'Мозиков Евгений Александрович'


# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.


def print_digits(number):
    """This is the implementation of task 1 easy

    Convert argument to string and print all the characters sequentially.
    No exceptions catching! Pass int value
    """
    print('Here is your number: {}'.format(number))
    for digit in str(number):
        print(digit)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


def swap_variables():
    """This is the implementation of task 2 easy

    Get two variables from user, swap and print them
    """
    a = int(input('Please enter first value: '))
    b = int(input('Please enter second value: '))
    print('Here are your variables: a - {}, b - {}'.format(a, b))
    a = a + b
    b = a - b
    a = a - b
    print('Here are swapped variables: a - {}, b - {}'.format(a, b))


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


def check_access():
    """This is the implementation of task 3 easy

    Get age from user, check if it is less then 18 or not, print warning message
    """
    age = int(input('Please enter your age: '))
    if age >= 18:
        print('Доступ разрешен')
    else:
        print('Извините, пользование данным ресурсом только с 18 лет')


if __name__ == '__main__':
    print_digits(random.randrange(999999999))
    print('---------------------------------------------')
    swap_variables()
    print('---------------------------------------------')
    check_access()
