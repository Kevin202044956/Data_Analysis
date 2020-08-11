##
## File: week9a.py (STAT 3250)
## Topic: Dates and Times
##

#### Dates and Times

import datetime
import pandas as pd  

#### The datetime library

t = datetime.time(1, 2, 3, 4) # '.time' is just the time (no date)
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
type(t)

today = datetime.date.today() # Gives today's date, not time
print(today)
type(today)
print('ctime:', today.ctime())  # All of these are dates only, no time
print('tuple:', today.timetuple())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)

rightnow = datetime.datetime.now() # Date and time
rightnow  # No format
print(rightnow) # Generic format
format = "%a %b %d %H:%M:%S %Y"  # the keys for formatting can be found online
                                 # at http://strftime.org/
print(rightnow.strftime(format)) # date/time with specified format

format = "%A %B %d %Y %H:%M:%S"
print(rightnow.strftime(format))

format = "%A %m-%d-%y %H:%M:%S"
print(rightnow.strftime(format))

# 'fromtimestamp' gives date/time in local time
datetime.datetime.fromtimestamp(1527517491)
datetime.datetime.fromtimestamp(0) # Start time, local time
datetime.datetime.utcfromtimestamp(0) # Start time, UTC

# We can also set the format.
datetime.datetime.fromtimestamp(1527517491).strftime(format)

#### The pandas version

# pandas provides a function that works in a similar way.  The argument
# 'unit' specifies the time units -- here it is seconds.  The default
# is UTC.
ts = pd.to_datetime(1481250949, unit='s')
print(ts)

# We can get a different format using 'strftime'
format = "%a %b %d %H:%M:%S %Y"
print(ts.strftime(format))

# Or just put the format in strftime
print(ts.strftime("%B %d %Y"))
print(ts.strftime("%B %-d %Y"))  # Day without the zero padding

# We can extract parts of the datetime object by specifying
# the part directly or through 'strftime'
ts
ts.month
ts.hour
ts.strftime('%Y')
ts.strftime('%b')

## Series of timestamps

# Suppose that we have a Series of timestamps to process.

timestamps = pd.Series([881250949,891717742,878887116,880606923,886397596])
timestamps

# We can try 'datetime.datetime' ....
datetime.datetime.utcfromtimestamp(timestamps)  # Nope

# The pandas 'to_datetime' will take a Series as input and produce a Series
# of numpy datetime objects as output.
dts = pd.to_datetime(timestamps, unit='s')
print(dts)

dts.strftime('%Y')