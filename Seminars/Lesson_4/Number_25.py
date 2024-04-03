'''
Задача №25.
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию
.split()
'''
def count_occurrences(input_str):
    words = input_str.split()
    occurrences = {}

    # Обходим каждый символ в каждом слове, считаем количество повторов и формируем новую строку
    result = []
    for word in words:
        for char in word:
            occurrences[char] = occurrences.get(char, 0) + 1
            suffix = f"_{occurrences[char]}" if occurrences[char] > 1 else ""
            result.append(char + suffix)

    print(' '.join(result))

# Получаем входную строку от пользователя
input_str = input("Введите строку символов: ")
count_occurrences(input_str)

