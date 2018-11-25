import random


# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


def squares(lst):
    print(f'Your list: {lst}')
    return list(i * i for i in lst)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


def fruits(first, second):
    print(f'First fruit list: {first}')
    print(f'Second fruit list: {second}')
    return list(i for i in first if i in second)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


def specific_list(lst):
    print(f'Your list: {lst}')
    return list(i for i in lst if i > 0 and i % 4 != 0 and i % 3 == 0)


if __name__ == '__main__':
    lst = list(random.randrange(10) for i in range(10))
    new_lst = squares(lst)
    print(f'New list: {new_lst}')
    print('--------------------------------------------------')
    fruits_list = ['apple', 'kiwi', 'apricot', 'mango', 'strawberry', 'banana', 'pineapple', 'orange', 'lemon']
    first = random.sample(fruits_list, random.randint(1, len(fruits_list)))
    second = random.sample(fruits_list, random.randint(1, len(fruits_list)))
    new_lst = fruits(first, second)
    print(f'New list: {new_lst}')
    print('--------------------------------------------------')
    lst = list(random.randint(-20, 20) for i in range(20))
    new_lst = specific_list(lst)
    print(f'New list: {new_lst}')
