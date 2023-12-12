import pandas as pd
import numpy as np

anime_data = pd.read_csv("anime_info.csv", header=0, sep=",")

numeric_columns = anime_data.select_dtypes(include='number')

var = np.var(numeric_columns)

print(var)