'''
Задача №63
1. Изобразите отношение households к population с помощью точечного графика
2. Визуализировать longitude по отношения к median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
'''

import pandas as pd
import seaborn as sns

df = pd.read_csv('/content/sample_data/california_housing_train.csv')

sns.set(style='whitegrid')
sns.scatterplot(x="households",	y="population",	data=df)

sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)

sns.histplot(data=df, x='housing_median_age')

sns.displot(x='median_house_value', data=df, hue='housing_median_age')

