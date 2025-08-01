import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset directly from local, dataset of 8000 Netflix titles listed up to 2021
netflix_full = pd.read_csv(r'netflix_titles.csv')
# Filtering the dataset for relevant columns

netflix = netflix_full[['title', 'release_year', 'director', 'country', 'duration']].copy()
# To avoid `SettingWithCopyWarning`, I used `.copy()` when creating filtered subsets of the DataFrame.
# This ensures that subsequent modifications are done safely, without ambiguity between copy and view.

# Using pd.set_option to improve data display in the console
pd.set_option('display.max_columns', None)

# Handling NaN values in the director column to avoid issues in the plots
netflix['director'] = netflix['director'].fillna('Not listed')
# The specific title had NaN duration, since it was a comedy stand-up I replaced with an average duration
netflix.loc[netflix['title'].str.contains("Louis C.K."), 'duration'] = "60 min"
# Creating a version with 'Unknown' included
netflix['country'] = netflix['country'].fillna('Unknown')
# Now there are no NaN values in the dataframe, time to separate movies and series

# Separating titles by 'Min' and 'Season'
netflix_filmes = netflix[netflix['duration'].str.contains('min', na=False)].copy()
netflix_series = netflix[netflix['duration'].str.contains('Season', na=False)].copy()

# Counting how many movies were released each year
filmes_por_ano = netflix_filmes['release_year'].value_counts().sort_index()

# Counting how many series were released each year
series_por_ano = netflix_series['release_year'].value_counts().sort_index()

conteudo_por_pais = netflix['country'].value_counts().reset_index()
conteudo_por_pais.columns = ['Country', 'Quantity']

top_paises = netflix['country'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_paises.values, y=top_paises.index, hue=top_paises.index, palette='viridis', legend=False)

plt.title('Top 10 Countries with Most Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.tight_layout()
plt.show()
