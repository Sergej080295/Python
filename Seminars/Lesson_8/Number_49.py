'''
Задача №49
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, 
имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
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
    print("5. Выход")

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
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
        