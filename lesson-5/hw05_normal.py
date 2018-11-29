from hw05_easy import go_to_dir, print_dir_content, delete_dir, create_dir


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def get_menu():
    menu = {
        'Перейти в папку': go_to_dir,
        'Просмотреть содержимое папки': print_dir_content,
        'Удалить папку': delete_dir,
        'Создать папку': create_dir,
        'Выйти': quit
    }
    return menu


def print_menu(menu):
    for i, action in enumerate(menu, 1):
        print(f'{i}. {action}')


def check_input(menu_len):
    choice = input()
    try:
        choice = int(choice)
        if 1 <= choice <= menu_len:
            return choice
        else:
            print('Please choose valid menu function!')
    except TypeError:
        print('Please choose valid menu function!')


if __name__ == '__main__':
    menu = get_menu()
    while True:
        print_menu(menu)
        choice = check_input(len(menu))
        if choice:
            key = list(menu.keys())[choice - 1]
            menu[key]()
