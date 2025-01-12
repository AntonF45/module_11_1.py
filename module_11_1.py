import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('titanic.csv')

# Вывод первых 2 строк DataFrame
print(df.head(2))

# Вывод последних 2 строк DataFrame
print(df.tail(2))

# выводим вторую строку целиком
print(df.loc[1])

# сортируем данные по столбцу 'Age'
dataframe_sorted = df.sort_values(by='Age')
print(dataframe_sorted)

# получаем размеры DataFrame с помощью shape
print(f'Размер DataFrame: {df.shape}')

# вывод основных статистических показателей
print(df.describe())
