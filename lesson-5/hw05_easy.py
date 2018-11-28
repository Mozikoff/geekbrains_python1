import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_and_del_dirs():
    for i in range(1, 10):
        os.makedirs(f'dir_{i}', exist_ok=True)
    files = os.listdir()
    print(files)
    for file in files:
        if os.path.isdir(file) and 'dir_' in file:
            os.rmdir(file)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_current_dirs():
    print(list(file for file in os.listdir() if os.path.isdir(file)))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_current_file():
    shutil.copyfile(__file__, f'{__file__}.copy')
    print(os.listdir())


# for task 1 normal
def go_to_dir():
    path = input()
    if os.path.exists(path) and os.path.isdir(path):
        os.chdir(path)
        print(f'Current dir is now {path}')
    else:
        print(f'{path} is not a dir!')


def print_dir_content():
    print('Current dir contains following items:')
    print(list(os.listdir()))


def delete_dir():
    path = input()
    if os.path.exists(path) and os.path.isdir(path):
        os.rmdir(path)
        print(f'{path} dir deleted!')
    else:
        print(f'{path} is not a dir!')


def create_dir():
    path = input()
    os.makedirs(path, exist_ok=True)
    print(f'{path} dir created!')


if __name__ == '__main__':
    make_and_del_dirs()
    list_current_dirs()
    copy_current_file()
