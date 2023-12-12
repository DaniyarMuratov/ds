import pandas as pd
import numpy as np

anime_data = pd.read_csv("anime_info.csv", header=0, sep=",")
vote = anime_data['vote']
percentile83 = np.percentile(vote, 83)
print (percentile83)