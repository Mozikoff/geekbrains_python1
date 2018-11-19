import string


# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?

# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра


def intersect(txt1, txt2):
    table = str.maketrans({key: None for key in string.punctuation})
    txt1 = txt1.translate(table)
    txt2 = txt2.translate(table)
    return set(txt1.lower().split()).intersection(set(txt2.lower().split()))


if __name__ == '__main__':
    txt1 = 'Some text about programming in Python!'
    txt2 = 'How about some coffee, Python?'
    print(intersect(txt1, txt2))
