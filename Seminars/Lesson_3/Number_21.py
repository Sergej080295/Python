"""
Задача №21. 
Напишите программу для печати всех уникальных значений в словаре. 
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
":" S007 "}] 

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально. 
Пользователь его не вводит
"""

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
values_list = []

for N in dictionary:
    values_list.extend(N.values())
values_list = set(values_list)
print (values_list)