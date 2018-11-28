from collections import Counter


# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.


def most_common_pass():
    passwords = []
    with open('pwd.txt', 'r') as file:
        for line in file:
            passwords.append(line.rstrip()[line.find(';') + 1:])
    print(Counter(passwords).most_common(10))


if __name__ == '__main__':
    most_common_pass()
