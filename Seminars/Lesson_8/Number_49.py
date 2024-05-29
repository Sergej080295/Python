'''
Задача №49
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, 
имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
для изменения и удаления данных
'''

# Функция для добавления новой записи
def add_contact():
    with open('phonebook.txt', 'a') as file:
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        patronymic = input("Введите отчество: ")
        phone_number = input("Введите номер телефона: ")
        file.write(f"{surname}, {name}, {patronymic}, {phone_number}\n")
    print("Запись успешно добавлена в справочник.")

# Функция для вывода всех записей из справочника
def display_contacts():
    with open('phonebook.txt', 'r') as file:
        for line in file:
            print(line.strip())

# Функция для поиска записи (имя, фамилия и пр..)
def search_contact(criteria):
    with open('phonebook.txt', 'r') as file:
        for line in file:
            contact = line.split(', ')
            if criteria in contact:
                print(line.strip())

# Функция для изменения записи
def edit_contact():
    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()
    line_number = int(input("Введите номер строки для изменения: "))
    if 0 < line_number <= len(lines):
        surname = input("Введите новую фамилию: ")
        name = input("Введите новое имя: ")
        patronymic = input("Введите новое отчество: ")
        phone_number = input("Введите новый номер телефона: ")
        lines[line_number - 1] = f"{surname}, {name}, {patronymic}, {phone_number}\n"
        with open('phonebook.txt', 'w') as file:
            file.writelines(lines)
        print("Запись успешно изменена.")
    else:
        print("Некорректный номер строки.")

# Функция для удаления записи
def delete_contact():
    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()
    line_number = int(input("Введите номер строки для удаления: "))
    if 0 < line_number <= len(lines):
        del lines[line_number - 1]
        with open('phonebook.txt', 'w') as file:
            file.writelines(lines)
        print("Запись успешно удалена.")
    else:
        print("Некорректный номер строки.")

# Добавляем возможность копирования контакта
def copy_contact(source_file, destination_file, line_number):
    with open(source_file, 'r') as source:
        lines = source.readlines()
        if 0 < line_number <= len(lines):
            with open(destination_file, 'a') as destination:
                destination.write(lines[line_number - 1])
            print("Запись успешно скопирована.")
        else:
            print("Некорректный номер строки.")

# Основная часть программы
while True:
    print("\nМеню:")
    print("1. Добавить новую запись")
    print("2. Вывести все записи")
    print("3. Поиск по критерию")
    print("4. Копировать запись в другой файл")
    print("5. Изменить запись")
    print("6. Удалить запись")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        search_criteria = input("Введите критерий для поиска: ")
        search_contact(search_criteria)
    elif choice == '4':
        source_file = 'phonebook.txt'
        destination_file = 'phonebook_new.txt'
        line_number = int(input("Введите номер строки для копирования: "))
        copy_contact(source_file, destination_file, line_number)
    elif choice == '5':
        edit_contact()
    elif choice == '6':
        delete_contact()
    elif choice == '7':
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
        