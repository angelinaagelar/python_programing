import pandas as pd
import random

"""Урок 15. Семинар. Построение графиков
| Задание 44 |
| --- |
| В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() |
"""

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})
data.head()

one_hot_data = pd.DataFrame()

categories = data['whoAmI'].unique()

for cate in categories:
  one_hot_data[cate] = (data['whoAmI'] == cate).astype(int)

print("\nOne-hot encoded DataFrame:")
print(one_hot_data.head())