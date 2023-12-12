import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

x = df['x']
y = df['y']

plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Данные')
plt.plot(x, 0.3 * x + 20, color='red', label='y = 0.3x + 20')
plt.title('Зависимость объема продаж от рекламных расходов')
plt.xlabel('Рекламные расходы')
plt.ylabel('Объем продаж')
plt.legend()
plt.grid(True)
plt.show()
