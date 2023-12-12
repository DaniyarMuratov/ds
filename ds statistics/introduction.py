import pandas as pd
import numpy as np

anime_data = pd.read_csv("anime_info.csv", header=0, sep=",")

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print (anime_data.describe())