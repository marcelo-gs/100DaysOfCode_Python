# -*- coding: utf-8 -*-
"""DataExploration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzizUrgec6tf1xH-KtLUUTnsCqhaKlAN
"""

import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
df.head()

""".head() shows the first 5 rows of a dataset/dataframe"""

df.shape

"""shape shows the number of rows and columns"""

df.columns

df.isna()

"""we're going to look for NaN (Not A Number) values in our dataframe. NAN values are blank cells or cells that contain strings instead of numbers. Use the .isna() method and see if you can spot if there's a problem somewhere."""

df.tail()

""".tail() shows the last 5 lines in dataset/dataframes"""

clean_df = df.dropna()
clean_df.tail()

""".dropna() removes the NaN rows"""

clean_df['Starting Median Salary']

clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[43]

clean_df['Undergraduate Major'][43]

clean_df.loc[43]

print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]

print(clean_df['Starting Median Salary'].min())
print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()])

clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

"""Majors with the Highest Potential"""

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

"""**Majors with the Greatest Spread in Salaries**"""

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

clean_df.groupby('Group').count()

clean_df.groupby('Group').mean()

"""We can tell Pandas to print the numbers in our notebook to look like 1,012.45 with the following line"""

pd.options.display.float_format = '{:,.2f}'.format

"""The PayScale dataset used in this lesson was from 2008 and looked at the prior 10 years. Notice how Finance ranked very high on post-degree earnings at the time. However, we all know there was a massive financial crash in that year. Perhaps things have changed. Can you use what you've learnt about web scraping in the prior lessons (e.g., Day 45) and share some updated information from PayScale's website in the comments below? """

# Main dataframe to collect all data
table_from_html = pd.read_html("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
df = table_from_html[0].copy()
df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]

# Add tables from other pages to main dataframe
for page_no in range(2, 35):
    table_from_html = pd.read_html(f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_no}")
    page_df = table_from_html[0].copy()
    page_df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
    df = df.append(page_df, ignore_index=True)

# Select necessary columns only
df = df[["Major", "EarlyCareerPay", "MidCareerPay"]]

# Clean columns
df.replace({"^Major:": "", "^Early Career Pay:\$": "", "^Mid-Career Pay:\$": "", ",": ""}, regex=True, inplace=True)

# Change datatype of numeric columns
df[["EarlyCareerPay", "MidCareerPay"]] = df[["EarlyCareerPay", "MidCareerPay"]].apply(pd.to_numeric)

df.nlargest(5, "EarlyCareerPay")

df.nlargest(5, "MidCareerPay")

"""----------------------------------------------------------

**Today's Learning Points**

Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.

Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.

You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]

You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]

The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()

You can sort the DataFrame with .sort_values() and add new columns with .insert()

To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method
"""