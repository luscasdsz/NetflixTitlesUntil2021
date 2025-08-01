import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the dataset directly from local, dataset of 8000 Netflix titles listed up to 2021
netflix_full = pd.read_csv(r'netflix_titles.csv')

# Filtering the dataset for relevant columns
netflix = netflix_full[['title', 'release_year', 'director', 'duration']].copy()
# To avoid the `SettingWithCopyWarning`, I used `.copy()` when creating filtered subsets of the DataFrame.
# This ensures that later modifications are safely done without ambiguity between copy and view.

# Using pd.set_option to improve data display in the console
pd.set_option('display.max_columns', None)

# Handling NaN values in the director column to avoid issues in plots
netflix['director'] = netflix['director'].fillna('Not listed')
# The specific title had NaN duration, since it was a comedy stand-up I replaced with an average duration
netflix.loc[netflix['title'].str.contains("Louis C.K."), 'duration'] = "60 min"
# Now there are no NaN values in the dataframe, time to separate movies and series

# Separating titles by 'min' and 'Season'
netflix_filmes = netflix[netflix['duration'].str.contains('min', na=False)].copy()
netflix_series = netflix[netflix['duration'].str.contains('Season', na=False)].copy()

# Counting how many movies were released each year
filmes_por_ano = netflix_filmes['release_year'].value_counts().sort_index()

# Counting how many series were released each year
series_por_ano = netflix_series['release_year'].value_counts().sort_index()

# Adding a decade column
netflix['decade'] = (netflix['release_year'] // 10) * 10

# Define if it's a series or movie based on duration
netflix['type'] = netflix['duration'].str.contains('Season', na=False)
netflix['type'] = netflix['type'].replace({True: 'Series', False: 'Movie'})

# Create the main plot
plt.figure(figsize=(10, 6))
sns.countplot(data=netflix, x='decade', hue='type')

# Visual adjustments
plt.title('Number of Titles per Decade (Movies vs Series)')

plt.show()
