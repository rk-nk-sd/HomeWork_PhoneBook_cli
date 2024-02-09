from logger import *
def interface():
    print('Добрый день это бот помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные\n'
          '3 - Обновить контакт\n'
          '4 - Удалить контакт\n'
          '5 - Копировать контакт')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 5:
        command = int(input('Ошибка! Ваш выбор: '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        update_data()
    elif command == 4:
        delete_data()
    elif command == 5:
        copy_data()
