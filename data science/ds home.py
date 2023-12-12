import matplotlib
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

degree = 2

coefficients = np.polyfit(x, y, degree)


def polynomial_regression(value, cf):
    result = 0
    for i in range(degree + 1):
        result += cf[i] * (value ** (degree - i))
    return result


x_pred = np.linspace(min(x), max(x), 100)
y_pred = [polynomial_regression(x_val, coefficients) for x_val in x_pred]

plt.scatter(x, y)
plt.plot(x_pred, y_pred, label=f'Дәрежесі-{degree} Полиномиальды регрессия', color='red')
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.legend()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
