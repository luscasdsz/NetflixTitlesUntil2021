# Netflix Titles Analysis - Country and Content Type

This project analyzes a dataset of around 8000 Netflix titles listed until 2021, focusing on the distribution of titles by country and type (movies vs series).

## Dataset

- Source: `netflix_titles.csv` (local CSV file)
- Contains title, release year, director, country, and duration information.

## What this script does

- Loads and filters the dataset for relevant columns.
- Cleans missing data in 'director' and 'country' columns.
- Separates titles into movies and series based on the 'duration' column.
- Counts the number of titles by country.
- Visualizes the top 10 countries with the most Netflix titles using a horizontal bar plot.
- Includes practical data cleaning to avoid pandas warnings and ensure safe dataframe operations.

## How to run

1. Make sure you have Python 3.x installed.
2. Install dependencies:
