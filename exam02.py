##
## File: exam02.py (STAT 3250)
## Topic: Exam 2
## Name: Kaiwen Zhu(kz8pr)

##  As discussed in class, Exam 2 will be fairly close in form to assignments:
##  there is no "in-class" or timed portion, and you are welcome to talk with
##  other students about solution strategies.  Two major differences from 
##  assignments:

##
##  (1) Course assistants only will provide help with code debugging but will
##      not provide a lot of help with code strategy.
##  (2) Grading will be stricter than with assignments.  In particular, the
##      code efficiency and elegance will be considered in grading to a 
##      greater degree than on assignments.  Also taken into account will be
##      using coding approaches covered in class, rather than something 
##      found online or in another course.
##
##  Grading of Exam 2: 5 questions will be selected for scoring from 0-5,
##  and 5 points will be added for overall completeness, for a total of 30.

##  Note: There is no blanket prohibition on the use of loops, but loops can
##  be inefficient and inelegant so excessive use when non-loop options exist
##  is likely to result in score reductions.  (The same goes for reading in 
##  data.  You should not do that more than once.)

##  The exam is due by Thursday March 28 at 11:30pm.  Exams marked late by
##  Collab will receive a 2 point deduction.  No exams may be submitted after
##  Friday, March 29 at 11:30am.

##  This exam requires the data file 'airline-stats.txt'.  This file contains
##  over 50,000 records of aggregated flight information, organized by airline, 
##  airport, and month.  The first record is shown below.

# =============================================================================
# airport
#     code: ATL 
#     name: Atlanta GA: Hartsfield-Jackson Atlanta International
# flights 
#     cancelled: 5 
#     on time: 561 
#     total: 752 
#     delayed: 186 
#     diverted: 0
# number of delays 
#     late aircraft: 18 
#     weather: 28 
#     security: 2 
#     national aviation system: 105 
#     carrier: 34
# minutes delayed 
#     late aircraft: 1269 
#     weather: 1722 
#     carrier: 1367 
#     security: 139 
#     total: 8314 
#     national aviation system: 3817
# dates
#     label: 2003/6 
#     year: 2003 
#     month: 6
# carrier
#     code: AA 
#     name: American Airlines Inc.
# =============================================================================

import pandas as pd
import numpy as np

text = pd.Series(open('airline-stats.txt').read().split('##########')) #read the text and split by specific element
record = text[~text.str[1].isnull()]    #extract the meaningful part

## 1.  Give the total number of hours delayed for all flights in all records.

group1 = record.str.split('total: ').str[2].str.split().str[0].astype(int)  #extract the series of the total minutes and change type
result1 = np.sum(group1)/60 #sum all minutes and get the hour
print(result1)  #print the result

'''
9991285.583333334 hours
'''

## 2.  Which airlines appear in at least 1000 records?  Give a table of airline
##     names and number of records for each, in order of record count (largest
##     to smallest).

group2 = record.str.split('name: ').str[-1].str.strip()   #extract the series of the airline name and strip the sapce
result2 = group2.value_counts()[group2.value_counts() > 1000]   #get the total numbers of each airline and pick greater than 1000
print(result2)  #print the result

'''
Delta Air Lines Inc.            4370
American Airlines Inc.          4296
United Air Lines Inc.           4219
US Airways Inc.                 3918
ExpressJet Airlines Inc.        3174
Southwest Airlines Co.          2900
JetBlue Airways                 2857
Frontier Airlines Inc.          2821
Continental Air Lines Inc.      2815
AirTran Airways Corporation     2801
Alaska Airlines Inc.            2678
SkyWest Airlines Inc.           2621
American Eagle Airlines Inc.    2379
Northwest Airlines Inc.         2288
Mesa Airlines Inc.              1682
Comair Inc.                     1671
Atlantic Southeast Airlines     1460
Hawaiian Airlines Inc.          1073
dtype: int64
'''
    
## 3.  For some reason, the entry under 'flights/delayed' is not always the same
##     as the total of the entries under 'number of delays'.  (The reason for
##     this is not clear.)  Determine the percentage of records for which 
##     these two values are different.

group3 = record.str.split('number of delays').str[1].str.split('minutes delayed').str[0]    #extract the the total minutes delayed
group4 = (group3.str.split().str[2].astype(int) + group3.str.split().str[4].astype(int)
+group3.str.split().str[6].astype(int) + group3.str.split().str[10].astype(int) + group3.str.split().str[12].astype(int))   #try to create a series which contains all minutes delayed
group5 = record.str.split('delayed: ').str[1].str.split().str[0].astype(int)    #extract the number of total delayed and change type to int
result3 = np.count_nonzero(np.array(group4) - np.array(group5))/len(record) *100      #calculate the difference of such two series and count the non_zero element
print(result3)  #print the result

'''
the percentage is 29.283690963286617
'''


## 4.  Determine the number of records for which the number of delays due to
##     late aircraft exceeds the number of delays due to weather.

group6 = record.str.split('late aircraft: ').str[1].str.split().str[0].astype(int)  #extract the number of late aircraft and change type to int
group7 = record.str.split('weather: ').str[1].str.split().str[0].astype(int)    #extract the number of weather delayed and change type to int
group8 = group6 - group7     #create the series which contains the difference of such two numbers
result4 = len(group8[group8>0]) #count the len of the series which is greater than 0
print(result4) #print the result

'''
46890
'''


## 5.  Find the top-10 airports in terms of the total number of minutes delayed.
##     Give a table of the airport names and the total minutes delayed, in 
##     order from largest to smallest.

df2 = pd.DataFrame({'airports':[],'total minutes':[]})     #create the dataframe 
group9 = record.str.split('name: ').str[1].str.split('flights').str[0].str.strip()  #extract the series which contains airline's name
group10 = record.str.split('total: ').str[2].str.split().str[0].astype(int)     #extract the series which contains the total minutes of each airline
df2['airports'] = group9       #store such series to dataframe
df2['total minutes'] = group10     #store such series to dataframe
result5 = df2['total minutes'].groupby(df2['airports']).sum().sort_values(ascending=False)[0:10]    #sort the dataframe from large to small and pick the top-10 results
print(result5)  #print the result

'''
airports
Chicago IL: Chicago O'Hare International                 66079561
Atlanta GA: Hartsfield-Jackson Atlanta International     61818488
Dallas/Fort Worth TX: Dallas/Fort Worth International    39246534
Newark NJ: Newark Liberty International                  33306693
San Francisco CA: San Francisco International            28980270
Denver CO: Denver International                          27020884
Los Angeles CA: Los Angeles International                26897269
Houston TX: George Bush Intercontinental/Houston         24121262
New York NY: LaGuardia                                   22335295
New York NY: John F. Kennedy International               19985703
Name: total minutes, dtype: int64
'''

## 6.  Find the top-10 airports in terms of percentage of on time flights.
##     Give a table of the airport names and percentages, in order from 
##     largest to smallest.

group11 = record.str.split('on time: ').str[1].str.split().str[0].astype(float) #extract the number of on time airport and change type to float
group12 = record.str.split('total: ').str[1].str.split().str[0].astype(float)   #extract the number of total airport and change type to float
df3 = pd.DataFrame({'airports':[],'on_time':[],'total':[],'percentage':[]})     #create a new dataframe
df3['airports'] = group9    #store the data the group 9 is from question 5
df3['on_time'] = group11    #store the data
df3['total'] = group12      #store the data
result6 = df3.groupby(df3['airports']).sum()  #sum all on_time and total series
result6['percentage'] = result6['on_time']/result6['total']*100 #get the percentage
print(result6['percentage'].sort_values(ascending=False)[0:10]) #sort such dataframe and get the top 10 results

'''
airports
Salt Lake City UT: Salt Lake City International                       84.249328
Phoenix AZ: Phoenix Sky Harbor International                          82.423895
Portland OR: Portland International                                   80.759415
Minneapolis MN: Minneapolis-St Paul International                     80.342827
Chicago IL: Chicago Midway International                              80.317165
Charlotte NC: Charlotte Douglas International                         80.310017
Baltimore MD: Baltimore/Washington International Thurgood Marshall    80.268309
Denver CO: Denver International                                       80.236443
Detroit MI: Detroit Metro Wayne County                                80.182134
Houston TX: George Bush Intercontinental/Houston                      80.117228
Name: percentage, dtype: float64
'''

## 7.  Find the top-10 airlines in terms of percentage of on time flights.
##     Give a table of the airline names and percentages, in order from 
##     largest to smallest.
  
df4 = pd.DataFrame({'airline':[],'on_time':[],'total':[]})  #create a new dataframe
group13 = record.str.split('name: ').str[-1].str.strip()    #extract the series which contains airline's name
df4['airline'] = group13     #store the airline's name
df4['on_time'] = group11     #store on_time number which from question 6
df4['total'] = group12       #store the total number which from question 6
result7 = df4.groupby(df4['airline']).sum()     #get the sum of on_time and total
result7['percentage'] = result7['on_time']/result7['total'] *100    #calculate the percentage
print(result7['percentage'].sort_values(ascending=False)[0:10])     #sort the result and print the top-10 result

'''
airline
Endeavor Air Inc.             84.050792
Alaska Airlines Inc.          81.888334
Virgin America                81.492009
Aloha Airlines Inc.           80.934150
Delta Air Lines Inc.          80.411719
SkyWest Airlines Inc.         80.102370
Southwest Airlines Co.        80.061932
America West Airlines Inc.    79.373011
Hawaiian Airlines Inc.        79.308415
US Airways Inc.               78.974549
Name: percentage, dtype: float64
'''

## 8.  Determine the average length (in minutes) of a weather-related delay.

index1 = record.str.split('weather: ').str[2].str.split().str[0].astype(float).sum()    #extract the weather delayed minutes and get the sum
index2 = record.str.split('weather: ').str[1].str.split().str[0].astype(float).sum()    #extract the number of weather delayed and get the sum
print(index1/index2)    #print the average length

'''
80.25100063808806
'''

## 9.  For each month, determine which airport had the highest percentage
##     of delays.  Give a table listing the month number, the airport name,
##     and the percentage.

group14 = record.str.split("delayed: ").str[1].str.split().str[0].astype(float)     #extract the number of delayed 
group15 = record.str.split("month: ").str[1].str.split().str[0] #extract the month number
df5 = pd.DataFrame({"month":group15,"airport":group9,"delayed":group14,"total":group12})    #create a new dataframe to store data group9 from question 5 group12 from question 6
df6 = df5["delayed"].groupby([df5["month"],df5["airport"]]).sum() / df5["total"].groupby([df5["month"],df5["airport"]]).sum()   #get the percentage of delyed for each airport in each month
res9 = pd.DataFrame(df6.sort_values(ascending=False)*100)   #create a new dataframe and sort the value
res9.index.names = ['month', 'airport'] #set index's name
res10 = res9.reset_index(level=['month', 'airport']).groupby("month").first()   #reset each index name and groupby month and get the first result of each group
print(res10) #print the result

'''
month                                                                    
1      Chicago IL: Chicago O'Hare International  27.392193
10      Newark NJ: Newark Liberty International  26.140379
11      Newark NJ: Newark Liberty International  26.961231
12      Newark NJ: Newark Liberty International  33.508850
2       Newark NJ: Newark Liberty International  27.909382
3       Newark NJ: Newark Liberty International  31.613341
4       Newark NJ: Newark Liberty International  30.250067
5       Newark NJ: Newark Liberty International  30.339172
6       Newark NJ: Newark Liberty International  32.249598
7       Newark NJ: Newark Liberty International  31.445250
8       Newark NJ: Newark Liberty International  27.601543
9       Newark NJ: Newark Liberty International  23.935120
'''



## 10. For each year, determine the percentage of flights delayed by weather.

year = record.str.split("year: ").str[1].str.split().str[0]   #extract the year from the raw data
df7 = pd.DataFrame({"year":year,"weather_delayed":group7,"total":group12})  #create the new dataframe, group7 from question 4, group12 from question 6
df8 = df7["weather_delayed"].groupby(df7["year"]).sum()/df7["total"].groupby(df7["year"]).sum() *100    #use groupby method and get the sum series, then get the percentage
print(df8)  #print the result

'''
year
2003    0.653742
2004    0.816713
2005    0.757056
2006    0.795570
2007    0.871017
2008    0.725152
2009    0.620590
2010    0.529282
2011    0.494533
2012    0.470042
2013    0.543351
2014    0.598251
2015    0.604453
2016    0.502287
dtype: float64
'''

## 11. Find the top-10 airports in terms of average length (in minutes) of 
##     security-related flight delays.  Give a table listing the airport name 
##     and average, sorted from largest to smallest.

security = record.str.split("security: ").str[2].str.split().str[0].astype(float)   #extract the series which contains the number of sercurity
security_delayed = record.str.split("security: ").str[1].str.split().str[0].astype(float)   #extract the series which contains the minutes of sercurity
df9 = pd.DataFrame({"airport":group9,"security_mintues":security,"security_delayed":security_delayed})  #create the dataframe which contains all data
res11 = df9["security_mintues"].groupby(df9["airport"]).sum()/ df9["security_delayed"].groupby(df9["airport"]).sum()    #use groupby method and sum the toatl series, then get the percentage
print(res11.sort_values(ascending=False)[0:10]) #sort value and print the top-10 results

'''
airport
Atlanta GA: Hartsfield-Jackson Atlanta International    49.742964
Boston MA: Logan International                          46.457082
Chicago IL: Chicago O'Hare International                46.311587
Miami FL: Miami International                           45.400826
Washington DC: Ronald Reagan Washington National        42.258621
San Francisco CA: San Francisco International           42.183099
Newark NJ: Newark Liberty International                 41.232283
New York NY: John F. Kennedy International              40.967069
New York NY: LaGuardia                                  40.853896
Washington DC: Washington Dulles International          40.224490
'''

## 12. Determine the top-10 airport/airline combinations that had the lowest
##     percentage of delayed flights.  Give a table listing the airport name,
##     the airline name, and the percentage of delayed flights, sorted in
##     order (smallest to largest) of percentage of delays.

df10 = pd.DataFrame({"airport":group9,"airline":group13,"delayed":group5,"total":group12})  #create the dataframe which store data, group5 from question 4, group 9 from question 5, group12 from question 6, group13 from question 7
res12 = df10["delayed"].groupby([df10["airport"],df10["airline"]]).sum()/df10["total"].groupby([df10["airport"],df10["airline"]]).sum()     #use groupby method and sum the delayed and total numbers, then get the percentage
res13 = pd.DataFrame(res12.sort_values()*100).reset_index(level = ["airport","airline"])    #create the result dataframe, reset the index and sor the values
print(res13[0:10])  #print the top 10 results

'''
airport name                                                                                               
Phoenix AZ: Phoenix Sky Harbor International        PinnacleAirlinesInc.                           0.000000
Las Vegas NV: McCarran International                          ComairInc.                           0.000000
New York NY: John F. Kennedy International            AlaskaAirlinesInc.                           4.347826
Salt Lake City UT: Salt Lake City International       AlaskaAirlinesInc.                           8.567829
Baltimore MD: Baltimore/Washington Internationa...    AlaskaAirlinesInc.                           8.689024
Fort Lauderdale FL: Fort Lauderdale-Hollywood I...       EndeavorAirInc.                           8.695652
Fort Lauderdale FL: Fort Lauderdale-Hollywood I...   SkyWestAirlinesInc.                           9.090909
Tampa FL: Tampa International                        SkyWestAirlinesInc.                          10.000000
Orlando FL: Orlando International                          VirginAmerica                          10.635226
Detroit MI: Detroit Metro Wayne County                   EndeavorAirInc.                          10.828148
'''
