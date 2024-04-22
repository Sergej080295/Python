'''
Задача №65
Написать EDA для датасета про пингвинов

Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы

Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
'''

penguins = sns.load_dataset('penguins')
penguins.info()

sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', data=penguins, palette='rainbow', hue='species', size=5)

sns.scatterplot(x='flipper_length_mm', y='body_mass_g', data=penguins, palette='rainbow', hue='species', size='body_mass_g')

sns.set(style='ticks', context='paper', palette='rainbow')
g = sns.PairGrid(penguins, diag_sharey=False, hue='species')
# g.map_lower(sns.kdeplot, cmap='Blues_d')
# g.map_upper(plt.scatter, alpha=0.5)
# g.map_diag(sns.kdeplot, lw=3);
g.map(sns.scatterplot)


sns.histplot(data=penguins, x='island', hue='species', palette='inferno')

import numpy as np
lst1 = list(penguins['bill_length_mm'])[:324]
lst1=np.array(lst1).reshape((18,18))
sns.heatmap(data=lst1, annot=True)
