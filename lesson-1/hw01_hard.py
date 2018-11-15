import doctest

__author__ = 'Мозиков Евгений Александрович'


# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?


def infinite_variable():
    """
    >>> a = float('inf')
    >>> a == a**2
    True
    >>> a == a*2
    True
    >>> a > 999999
    True"""
    a = float('inf')
    print(a == a ** 2)
    print(a == a * 2)
    print(a > 999999)
    print(a)


if __name__ == '__main__':
    doctest.testmod()
    infinite_variable()
