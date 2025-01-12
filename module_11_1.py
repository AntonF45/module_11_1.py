import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('titanic.csv')

# Вывод первых 2 строк DataFrame
print(df.head(2))

# Вывод последних 2 строк DataFrame
print(df.tail(2))

# получаем размеры DataFrame с помощью shape
print(f'Размер DataFrame: {df.shape}')

# вывод основных статистических показателей
print(df.describe())

# создание DataFrame
dataframe = pd.DataFrame({'M': [100, 120, 130], 'L': [140, 150, 165]})

# запись данных в файл CSV
dataframe.to_csv('output.csv', index=False)


