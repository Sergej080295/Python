'''
Задача №61
1. Определить какое максимальное и минимальное значение median_house_value
2. Показать максимальное median_house_value, где median_income = 3.1250
3. Узнать какая максимальная population в зоне минимального значения median_house_value
'''

print(df['median_house_value'].max())
print(df['median_house_value'].min())
df[df['median_income']==3.1250]['median_house_value']
df[df['median_house_value']==df['median_house_value'].min()]['population'].max()