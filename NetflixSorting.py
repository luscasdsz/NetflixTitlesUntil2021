import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the dataset directly from local, dataset of 8000 Netflix titles listed up to 2021
netflix_full = pd.read_csv(r'netflix_titles.csv')

# Filtering the dataset for relevant columns
netflix = netflix_full[['title', 'release_year', 'director', 'duration']].copy()
# To avoid `SettingWithCopyWarning`, I used `.copy()` when creating filtered subsets of the DataFrame.
# This ensures that later modifications are safely done without ambiguity between copy and view.

# Using pd.set_option to improve data display in the console
pd.set_option('display.max_columns', None)

# Handling NaN values in the director column to avoid issues in plots
netflix['director'] = netflix['director'].fillna('Not listed')
# The specific title had NaN duration, since it was a comedy stand-up I replaced it with an average duration
netflix.loc[netflix['title'].str.contains("Louis C.K."), 'duration'] = "60 min"
# Now there are no NaN values in the dataframe, time to separate movies and series

# Separating titles by 'min' and 'Season'
netflix_films = netflix[netflix['duration'].str.contains('min', na=False)].copy()
netflix_series = netflix[netflix['duration'].str.contains('Season', na=False)].copy()

# Counting how many movies were released each year
films_per_year = netflix_films['release_year'].value_counts().sort_index()

# Counting how many series were released each year
series_per_year = netflix_series['release_year'].value_counts().sort_index()

# Create a figure with size 12x6 inches (adjusts to avoid cramped or unreadable plots)
plt.figure(figsize=(12, 6))

# Plot the line of movie releases per year. marker='o' adds dots for readability.
plt.plot(films_per_year.index, films_per_year.values, label='Movies', marker='o')

# Plot the line for series releases, using squares as markers.
plt.plot(series_per_year.index, series_per_year.values, label='Series', marker='s')

# Add the title to the chart
plt.title('Number of Releases per Year (Netflix)')

# Define axis labels
plt.xlabel('Release Year')
plt.ylabel('Number of Releases')

# Add the legend (Movies / Series)
plt.legend()

# grid(True) activates grid lines, tight_layout() adjusts elements to avoid overlap, show() displays the plot.
plt.grid(True)
plt.tight_layout()
plt.show()





