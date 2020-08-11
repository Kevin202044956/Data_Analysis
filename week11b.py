##
## File: week11a.py (STAT 3250)
## Topic: Regular Expressions - Part 2a
##


import pandas as pd  # usual pandas

## Months

# A few candidates for months
months = pd.Series(["16", "05", "10", "58"])    


# The regular expression to check the form to determine if it is
# a month
months.str.contains("(0[1-9]|1[012])") # allows "0X" or 10,11,12 


## Dates


# Now for some candidates for dates
dates = pd.Series(["12-28", "15-19", "10-31", "03-17"])    


# This is a sloppy check, it will allow things like 10-78,
# Note: "\d" is any digit
dates.str.contains("(0[1-9]|1[012])-\d\d")    


# This is a more careful check, but it does still alow 02-30
dates.str.contains("(0[1-9]|1[012])-([0-2]\d|3[01])")


## Dates With Years   


dateswithyears = pd.Series(["12-28-2019", "07-39-1996", "06-22-1968", "03-17-1872"])
    

# This checks for years in the 1900's or 2000's only
dateswithyears.str.contains("(0[1-9]|1[012])-([0-2]\d|3[01])-(19|20)\d\d")    
    

    
    
    
    






