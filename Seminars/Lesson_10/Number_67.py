'''
Задача №67
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)

Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
'''

penguins.loc[penguins['bill_length_mm'] >= 42, 'height_group'] = 'high'
penguins.loc[(penguins['bill_length_mm'] < 42) & (penguins['bill_length_mm'] >= 35), 'height_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'low'
sns.histplot(data=penguins, x='height_group', hue='sex', multiple='stack')

sns.histplot(data=penguins, x='bill_length_mm', hue='height_group', multiple='stack')
