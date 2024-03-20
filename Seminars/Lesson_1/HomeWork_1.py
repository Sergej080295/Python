n = 123
num1 = n // 100 # сотни
num2 = (n % 100) // 10 # десятки
num3 = n % 10 # единицы
res = num1 + num2 + num3
print (res)