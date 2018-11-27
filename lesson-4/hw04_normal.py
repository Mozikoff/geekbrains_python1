import pprint
import random
from datetime import datetime as dt


# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random


def longest_seq(str):
    dict = {}
    prev = str[0]
    seq = prev
    length = len(seq)
    for i in str[1:]:
        if i == prev:
            seq += i
            length += 1
        else:
            if seq in dict:
                dict[seq] = length if length > dict[seq] else dict[seq]
            else:
                dict[seq] = length
            seq = i
            length = 1
        prev = i
    return max(dict.keys(), key=(lambda key: dict[key]))


def find_in_file(sym_count):
    file_name = f'task1_normal_{dt.timestamp(dt.now())}'
    with open(file_name, 'w') as file:
        for _ in range(sym_count - 1):
            file.write(str(random.randint(0, 3)))
    with open(file_name, 'r') as file:
        data = file.read(sym_count)
    return longest_seq(data)


# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте,
# остальные элементы тоже рандомные. Пользователь вводит размер


def random_matrix(length):
    result = []
    for i in range(length):
        result.append([])
        for j in range(length):
            result[i].append([])
            result[i][j] = random.randint(1, 100)
    for row in range(length):
        zero_index = random.randrange(length)
        result[row][zero_index] = 0
    return result


if __name__ == '__main__':
    str = find_in_file(20)
    print(f'The longest sequence is: {str} having length {len(str)}')
    print('-----------------------------------------------')
    matrix = random_matrix(10)
    pprint.pprint(matrix)
