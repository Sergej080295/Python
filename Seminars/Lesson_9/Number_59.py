'''
Задача №59
1. Проверить есть ли в файле пустые значения 
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
'''

df.isnull().sum()
df.loc[df['median_income']<2, 'median_house_value']
df[df.columns[:2]]
df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]