'''
Задача №35
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

Input: 5
Output: yes
'''

def is_prime(n):
    if n <= 1:
        return "no"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "no"
    return "yes"

# Ввод числа
number = int(input("Введите число: "))

# Проверка является ли число простым
result = is_prime(number)
print(result)