##
## File: week10a.py (STAT 3250)
## Topic: Various Topics
##

#### Zip codes

import pandas as pd

## Reading the zip code file

zips = pd.read_csv('zipcodes.txt')
zips  # There is a lot of stuff we don't need.

# The optional argument 'usecols' allows you to specify specific columns
# for importing, and ignore the rest.  Here we select the columns that
# have the zip code and the state, the columns indexed by 1 and 4.
zips = pd.read_csv('zipcodes.txt', usecols = [1,4])
zips

# Zip codes sometimes have leading zeros -- for instance, a zip
# code for Amherst, MA is 01002.  Pandas sees the zip codes as
# numbers, and drops the leading zeros.  We may want to load 
# the zip codes as strings, since that will match the format in 
# the file 'users.dat' file.
zips = pd.read_csv('zipcodes.txt',
                  usecols = [1,4],
                  converters={'Zipcode':str})
zips

zips = zips.drop_duplicates()

zipSer = pd.Series(zips['State'].values, index=zips['Zipcode'])


#### Specialized function: Is a string a number?
df = pd.DataFrame({'gender':['M','F','F','F','M','F'],
                   'age':['25','38','21','52','46','19'],
                   'zip':['22904','00327','V7J2K','49921','T9E8L','97752']})
df

# There are occasions when we need to check if a string is actually a digit
# so that it can be converted.  The function 'isdigit' will do this.
str.isdigit("23")  # Yes!
str.isdigit("STAT3250")  # No!

# This function is not vectorizable, but it will work with 'apply'.  Let's 
# test this on the column df['zip']

df['zip'].apply(str.isdigit)  # True = a digit; False = not a digit
~df['zip'].apply(str.isdigit) # Now True are the non-digits.


#### Regular expressions (very brief intro)

# A future assignment involves translating zip codes into states of residence.
# In previous data sets a few of the "zip codes" were really a postal code
# for a location in Canada.  These can be identified by having one or more 
# alphabetic characters ("A-Z" or "a-z") in the zip code.  The function 
# 're.search' shown below will determine if a string has any letters in it.

import re # re = "regular expression" which can be used to search

mystr = "00345" # No letter present -- U.S.
if re.search('[a-zA-Z]+', mystr):  # we will discuss regular expression syntax
    print("Canadian postal code")  # in the near future
else:
    print("U.S. zip code")

mystr = "T5L78" # Letter present -- call it Canada
if re.search('[a-zA-Z]+', mystr):
    print("Canadian postal code")
else:
    print("U.S. zip code")





