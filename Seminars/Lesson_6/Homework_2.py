'''
Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

def find_indices(list1, min_number, max_number):
    indices = []
    for i, num in enumerate(list1):
        if min_number <= num <= max_number:
            indices.append(i)
    return indices

list1 = list(map(int, input("Введите список чисел через пробел: ").split()))
min_number = int(input("Введите минимальное значение: "))
max_number = int(input("Введите максимальное значение: "))

result = find_indices(list1, min_number, max_number)
print(result)

