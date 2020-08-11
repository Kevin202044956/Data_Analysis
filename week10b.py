##
## File: week10b.py (STAT 3250)
## Topic: Dates and Directory Searches
##

#### Before We Start

# 1) In your computer's folder for STAT 3250, create a new folder "Stocks".
# 2) Place in the Stocks folder the files 'AA.csv', 'HSIC.csv', and 'WFM.csv'
# 3) Change your working directory to the Stocks folder.

#### More on Dates

import pandas as pd

# Here we use data from the file 'AA.csv' that contains stock prices from 
# a large airline.

stocks = pd.read_csv('AA.csv') # File of stock prices
stocks

# Here's the data types.
stocks.dtypes # Default data types for the columns
stocks.loc[0,'Date'] - stocks.loc[1,'Date'] # Not a date!

# Here's one way to convert the column so that Pandas recognizes
# the entries as dates.
stocks['Date'] = pd.to_datetime(stocks['Date']) # Convert to dates
stocks.dtypes

# We can identify the month, year, and day of the week:
stocks['Date'].dt.month
stocks['Date'].dt.year
stocks['Date'].dt.dayofweek # file dates in reverse chronological order

# It's possible to use inequalities on dates
stocks['Date'] < '2014-12-10'
(stocks['Date'] < '2014-12-19') & (stocks['Date'] > '2014-12-08')

# The above combines well with masking
stocks[stocks['Date'].dt.year == 2012]
stocks[(stocks['Date'] < '2014-12-19') & (stocks['Date'] > '2014-12-08')]
stocks.loc[stocks['Date'].dt.dayofweek == 0, 'Open']

# And we can do arithmetic
a = stocks.loc[0,'Date'] - stocks.loc[7,'Date']
a
b = stocks.loc[0,'Date'] - stocks.loc[5,'Date']
b

# We can do arithmetic with the 'Timedelta's
a/b 
(a-b)
(a+b)*4
a.days  # This extracts the value without the Timedelta


#### Concatenating Data Frames

# Define df1 and df2
df1 = pd.DataFrame({'J': [3,5,6,7],
                    'K': [8,3,2,5],
                    'L': [6,8,6,3]})
df1
df2 = pd.DataFrame({'J': [3,4,6,7,8],
                    'K': [4,7,0,11,3],
                    'L': [5,5,6,2,8]})
df2

# Concatenate df1 and df2 by rows
newdf = pd.concat([df1,df2])
newdf

# We can concatenate by columns, but we get odd results
newdf = pd.concat([df1,df2], axis=1)
newdf
newdf['J']

#### Searching directories

import glob # 'glob' searches for files

# Reminder: Change to directory 'Stocks'

# '*.csv' selects files ending in '.csv'
filelist = glob.glob('*.csv') # 'glob.glob' is the directory search
filelist

# The above list allows us to iterate through the files to read
# them in, one at a time.
for f in filelist:
    df = pd.read_csv(f)
    print(df,"\n")

# We can concatenate the dataframes into one large dataframe
df = pd.DataFrame()
for f in filelist:
    newdf = pd.read_csv(f)
    df = pd.concat([df,newdf])
df
