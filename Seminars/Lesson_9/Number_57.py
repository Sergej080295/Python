'''
Задача №57
1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
'''

import pandas as pd
df = pd.read_csv('sample_data/california_housing_test.csv')
df.head(n = 10)
df.shape
#(3000, 9)
df.dtypes
# longitude             float64
# latitude              float64
# housing_median_age    float64
# total_rooms           float64
# total_bedrooms        float64
# population            float64
# households            float64
# median_income         float64
# median_house_value    float64
# dtype: object