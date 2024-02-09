from data_create import input_user_data
import linecache
def input_data():
    name, surname, phone,address = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                f'1 Вариант:\n'
                f'{name}\n'
                f'{surname}\n'
                f'{phone}\n'
                f'{address}\n\n'
                f'2 Вариант:\n'
                f'{name};{surname};{phone};{address}\n\n'
                f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file: # а - от слова append
            file.write(
                f'{name}\n'
                f'{surname}\n'
                f'{phone}\n'
                f'{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')

def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

def delete_data():
    item = input(f'Введите имя или фамилию: ')
    book = int(input(f'\nВ каком спаравочнике нужно удалить контакт?\n'
                    f'Варианты 1 или 2\n'
                    f'Ваш выбор: '))
    result = []
    if book == 1:
        separator = '\n\n'
        filename = 'data_first_variant.csv'
    else:
        separator = '\n'
        filename = 'data_second_variant.csv'

    with open(f'{filename}', 'r') as file:
        filedata = file.read()
        filedata = filedata.split(f'{separator}')
        for contact_info_block in filedata:
            if contact_info_block.find(f'{item}') > -1:
                continue
            result.append(contact_info_block)
            result.append(f'{separator}')

    with open(f'{filename}', 'w') as file:
        result = ''.join(result).strip()
        result = f'{result}{separator}'
        file.write(result)


def update_data():
    src = input(f'Введите имя или фамилию: ')
    dest = input(f'Введите новое имя или фамилию: ')
    book = int(input(f'\nВ каком спаравочнике нужно удалить контакт?\n'
                    f'Варианты 1 или 2\n'
                    f'Ваш выбор: '))
    if book == 1:
        separator = '\n'
        filename = 'data_first_variant.csv'
    else:
        separator = ';'
        filename = 'data_second_variant.csv'

    with open(f'{filename}', 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(f'{src}{separator}', f'{dest}{separator}')

    with open(f'{filename}', 'w') as file:
        file.write(filedata)

def copy_data():
    item = input(f'Введите имя или фамилию: ')
    book = int(input(f'\nУкажите источник из которого нужно скопировать контакт?\n'
                     f'Варианты 1 или 2\n'
                     f'Ваш выбор: '))
    result = []
    if book == 1:
        end_block_data_separator = '\n\n'
        src_separator = '\n'
        dest_separator = ';'
        src = 'data_first_variant.csv'
        dest = 'data_second_variant.csv'
    else:
        end_block_data_separator = '\n'
        src_separator = ';'
        dest_separator = '\n'
        src = 'data_second_variant.csv'
        dest = 'data_first_variant.csv'

    with open(f'{src}', 'r') as file:
        filedata = file.read()
        filedata = filedata.split(f'{end_block_data_separator}')
        for contact_info_block in filedata:
            if contact_info_block.find(f'{item}') > -1:
                result.append(contact_info_block.replace(src_separator, dest_separator))
                # result.append(f'{end_block_data_separator}')


    with open(f'{dest}', 'a') as file:
        result = ''.join(result)
        if book == 1:
            result = ''.join(f'{result}\n')
            print(f'book == 1: => {end_block_data_separator}{result}')
        else:
            result = ''.join(f'{result}\n\n')
            print(f'book == 2: => {end_block_data_separator}{result}')
        # result = f'{end_block_data_separator}{result}'
        file.write(result)