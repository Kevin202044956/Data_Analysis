##
## File: week08a.py (STAT 3250)
## Topic: Misc. Commands; Merging data frames
## 

import numpy as np # load numpy as np
import pandas as pd # load pandas as pd

#### Extracting a substring; changing the data type

s = pd.Series(['A345EF076T89  24Mar1988',
              'X76TYS54ZL   08Jul2013',
              'TY76007GHEQ  13Dec2009',
              'HJ119TKJU8    02May1998',
              'GGTE45T1038,  21Oct1974'])

s.str.split()  # Split each list item on spaces

# Suppose we just want the year?  Splitting on spaces does not work, but
# we can count back characters from the end of each string.
years = s.str[-4:] # years always in 4 positions 
years

# Here is the mean of the years
np.mean(years)  #Hmm....

# The entries in years are strings, we need them to be floating point
# or integers to get the mean we want
years = years.astype(float)
np.mean(years)

#### Concatenating lists

# Start by creating a Series of lists
d = s.str.split()
d

# The "sum" command will apply "+" to the lists, which concatenates them.
sum(d,[])

#### Renumbering the index on a dataframe

sub = s[[0,1,3,4]] # extract a subSeries
sub

# We can reset the index to 0, 1, 2,...
sub.index = range(len(sub)) 
sub

#### Merging data sets

# Let's start with two simple data frames, to use as an illustration.
df1 = pd.DataFrame({'student':['Jim','Jane','Bob','Ann'],
                    'major':['English','Math','Math','CompSci']})
df1

df2 = pd.DataFrame({'student':['Ann','Bob','Jim','Jane'],
                    'year':[2,3,4,3]})
df2

# Both data frames have a column 'student' with the same students
# names in each.  The function 'pd.merge' recognizes the common
# column, and creates a new data frame that combines df1 and df2.
df3 = pd.merge(df1,df2)
df3

# Now suppose we have another data frame 'df4' that includes the
# name of majors and the building.
df4 = pd.DataFrame({'building':['Bryan','Kerchof','Rice'],
                    'major':['English','Math','CompSci']})
df4

# If we apply 'pd.merge' to df3 and df4, the two data frames
# are merged together based on the common column 'major'.
df5 = pd.merge(df3,df4)
df5

# Let's add one more data frame, this one with the student's
# favorite classes.
df6 = pd.DataFrame({'student':['Ann','Bob','Bob','Jim','Jane','Jane','Jane'],
                    'fav':['STAT 3250','MATH 4140','MATH 3350','SOC 2001',
                           'MATH 4140','MATH 3100','MATH 3310']})
df6

# Here's what we get if we merge df5 and df6:
df7 = pd.merge(df5,df6)
df7

# Aside: You can specify the merge key, if the default is not what
# you want.  (Or you just want it to be explicit.)
df7 = pd.merge(df5,df6, on='student')
df7

df8 = pd.DataFrame({'school':['College','College','College','College','SEAS'],
                    'major':['English','Math','Math','CompSci','CompSci']})
df8

# There is a duplicate row in df8.  We can remove this using 
# 'drop_duplicates()'
df8 = df8.drop_duplicates() 
df8

# Here's what we get when we merge df7 and df8:
df9 = pd.merge(df7,df8, on='major')
df9

# This new data frame might not be what we want -- Anne's school
# of enrollment is not clear.  The moral: Be careful with merging, and
# make sure it's doing what you want!
