'''
Задача 44
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

print(data.head(n=10))
# Создаем таблицу
one_hot_data = pd.crosstab(data.index, data['whoAmI'], margins=False)
# Задаем имя столбцам
one_hot_data.columns = ['whoAmI_' + str(col) for col in one_hot_data.columns]
print(one_hot_data)