import random


# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
#
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2. банан
# 3. киви
# 4. арбуз
#
# Подсказка: воспользоваться методом .format()


def fruit_list(lst):
    cnt = 0
    for fruit in lst:
        cnt += 1
        print(f'{cnt}. {fruit}'.rjust(10))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


def minus(lst1, lst2):
    print(lst1)
    print(lst2)
    for elem in lst2:
        if elem in lst1:
            lst1.remove(elem)
    print(lst1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def even_list(lst):
    print(lst)
    result = []
    for elem in lst:
        if elem % 2 == 0:
            result.append(elem // 4)
        else:
            result.append(elem * 2)
    return result


if __name__ == '__main__':
    fruits = ['яблоко', 'банан', 'киви', 'арбуз']
    fruit_list(fruits)
    print('-----------------------------------------------------')
    lst1 = [1, 2, 3, 4, 4, 6]
    lst2 = [2, 6, 9]
    minus(lst1, lst2)
    print('-----------------------------------------------------')
    lst = list(random.randint(0, 100) for i in range(10))
    new_list = even_list(lst)
    print(new_list)
