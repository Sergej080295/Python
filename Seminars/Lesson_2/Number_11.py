'''
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по 
счету числом Фибоначчи оно является, то есть 
выведите такое число n, что φ(n)=A. Если А не 
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
'''

A = int(input("Введите натуральное число A (>1): "))

fibonacci = [0, 1]
while fibonacci[-1] < A:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if A in fibonacci:
    index = fibonacci.index(A) + 1
    print("Output:", index)
else:
    print("Output: -1")

