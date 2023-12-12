import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('data.csv')


df.plot(x ='x', y='y', kind='line'),
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()
