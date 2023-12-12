import pandas as pd
import numpy as np

anime_data = pd.read_csv("anime_info.csv", header=0, sep=",")

view_stats = anime_data['view'].describe()
vote_stats = anime_data['vote'].describe()
rating_stats = anime_data['rating'].describe()

percentile10 = np.percentile(vote_stats, 10)

print("View:")
print(view_stats)
print("\nVote:")
print(vote_stats)
print("\nRating:")
print(rating_stats)
print("\nVote 10%:")
print(percentile10)