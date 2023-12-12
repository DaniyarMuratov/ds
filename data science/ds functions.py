import pandas as pd

data = {
    'Имя': ['Данияр', 'Досымжан', 'Аманжол', 'Дамир'],
    'Возраст': [19, 20, 18, 19],
    'Оценка': [92, 95, 90, 94]
}

df = pd.DataFrame(data)
print("Структурированные данные:")
print(df)

max_score = df['Оценка'].max()
print("Максимальная оценка:", max_score)

min_score = df['Оценка'].min()
print("Минимальная оценка:", min_score)

average_score = df['Оценка'].mean()
print("Средняя оценка:", average_score)
