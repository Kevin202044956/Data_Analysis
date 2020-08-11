#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:35:53 2019

@author: Kaiwen Zhu(kz8pr)
"""
#import all method we need
import glob
import pandas as pd

filelist = glob.glob('Stocks/*.csv')    #import the file list
df = pd.DataFrame() #create a new dataframe
name = []   #create the name list
for f in filelist:  #for loop
    newdf = pd.read_csv(f)  #read csv file
    newdf['ticker'] = f.split('/')[1].split('.')[0] #extract the name from the address
    df = pd.concat([df,newdf])  #concat the dataframe
    name.append(f)  #append the name

##1. Find the mean for the Open, High, Low, and Close entries for all records for all stocks.
    
mean_open = df['Open'].mean()   #get the mean value of the open
mean_High = df['High'].mean()   #get the mean value of the high
mean_Low = df['Low'].mean()   #get the mean value of the low
mean_Close = df['Close'].mean()     #get the mean value of the close
print(mean_open,mean_High, mean_Low, mean_Close)    #print the result
'''
Open: 50.863852209060646
High: 51.45941172575049
Low: 50.25336771426306
Close: 50.876481580134694
'''

##2. Find the top-5 and bottom-5 stocks in terms of their average Close price. 
## Give tables showing the stock ticker symbol and the average Close price.

res2 = df['Close'].groupby(df['ticker']).mean().sort_values(ascending=False)[0:5]   #get the close and use groupby method and the mean value
res3 = df['Close'].groupby(df['ticker']).mean().sort_values()[0:5]  #use the groupby method and get the bottom-5 result
print(res2,res3)    #print the result
'''
top-5:
ticker
CME     253.956017
AZO     235.951950
AMZN    185.140534
BLK     164.069088
GS      139.146781
Name: Close, dtype: float64

bottom-5:
ticker
FTR      8.969515
F       11.174158
XRX     11.291864
ETFC    12.808103
HBAN    13.697483
Name: Close, dtype: float64
'''

## 3. Find the top-5 and bottom-5 stocks in terms of the day-to-day volatility of the price, 
## which we define to be the mean of the daily differences High - Low for each stock. Give tables 
## for each, as in the previous problem.

df['Volatility'] = df['High'] - df['Low']   #use the formula to get the volatility
res4 = df['Volatility'].groupby(df['ticker']).mean().sort_values(ascending=False)[0:5]  #use groupby method to get the top-5 mean value
res5 = df['Volatility'].groupby(df['ticker']).mean().sort_values()[0:5] #use groupby method to get the bottom-5 mean value
print(res4,res5)    #print the result
'''
top-5:
ticker
CME     7.697287
AMZN    4.691407
BLK     4.470693
AZO     4.330294
ICE     4.056189
Name: Volatility, dtype: float64

bottom-5:
ticker
FTR     0.205275
XRX     0.308743
F       0.323567
HBAN    0.343893
NI      0.363250
Name: Volatility, dtype: float64
'''

## 4.Repeat the previous problem, this time using the relative volatility, which we define to be 
## the mean of for each day. As above, provide tables.

df['Volatility2'] = (df['High'] - df['Low'])/(0.5*(df['Open'] + df['Close']))   #use the formula to get the relative volatility
res6 = df['Volatility2'].groupby(df['ticker']).mean().sort_values(ascending=False)[0:5] #use groupby method to get the top-5 mean value
res7 = df['Volatility2'].groupby(df['ticker']).mean().sort_values()[0:5]    #use groupby method to get the bottom-5 mean value
print(res6,res7)    #print the result
'''
top-5:
ticker
AAL     0.055533
LVLT    0.054870
EQIX    0.051295
REGN    0.048172
ETFC    0.045381
Name: Volatility2, dtype: float64

bottom-5:
ticker
GIS    0.013966
PG     0.014192
K      0.014992
CL     0.015521
WEC    0.015761
Name: Volatility2, dtype: float64   
'''

## 5. For each day the market was open in October 2008, find the average daily Open, 
## High, Low, Close, and Volume for all stocks.

df['Date'] = pd.to_datetime(df['Date']) #create the datatime 
group5 = df[(df['Date'].dt.year == 2008)&(df['Date'].dt.month == 10)]   #extract the specific time
temp5 = group5.groupby(group5['Date']).mean()[['Open','High','Low','Close','Volume']]   #use groupb method and get the mean value
print(temp5)    #print the result

'''
                 Open       High        Low      Close        Volume
Date                                                                
2008-10-01  43.147874  44.089999  41.845493  43.095090  7.319004e+06
2008-10-02  43.033478  43.443991  40.642233  41.126958  9.555247e+06
2008-10-03  41.555534  42.923984  39.882176  40.264390  9.184641e+06
2008-10-06  39.408827  40.564248  36.730878  39.176739  1.176339e+07
2008-10-07  39.427268  40.293947  36.644575  36.933873  1.091851e+07
2008-10-08  36.106591  38.785221  35.062443  36.676517  1.378626e+07
2008-10-09  37.250109  38.002160  33.437178  33.848607  1.281094e+07
2008-10-10  32.581401  35.952582  30.432287  33.992102  1.820152e+07
2008-10-13  35.486543  38.041322  34.122389  37.548197  1.148344e+07
2008-10-14  38.581369  39.626962  35.513443  36.784888  1.240928e+07
2008-10-15  36.149596  36.757105  32.879340  33.197032  1.051697e+07
2008-10-16  33.485713  35.096629  31.415127  34.599193  1.258398e+07
2008-10-17  33.735344  36.184362  32.729962  34.400653  9.973754e+06
2008-10-20  34.989340  36.357728  33.968497  35.909339  7.657442e+06
2008-10-21  35.390477  36.344741  34.189521  34.665477  7.599813e+06
2008-10-22  33.751940  34.344688  31.386153  32.373295  9.425614e+06
2008-10-23  32.889517  33.987036  30.561443  32.516369  1.189890e+07
2008-10-24  30.046028  32.498308  29.403749  31.395146  9.726575e+06
2008-10-27  30.638140  31.924868  29.501411  29.877173  8.362392e+06
2008-10-28  30.860222  33.145389  29.345018  32.955575  1.091700e+07
2008-10-29  32.864871  34.887581  31.854395  33.179376  1.036944e+07
2008-10-30  34.273941  35.292079  32.884269  34.284817  8.928569e+06
2008-10-31  33.995771  35.761028  33.294631  34.976910  9.213693e+06
'''

## 6. For 2011, find the date with the maximum average relative volatility for all stocks and the 
## date with the minimum average relative volatility for all stocks. (Consider only days when the 
## market is open.)


group6 = df[df['Date'].dt.year == 2011]  #extract the specific  time
res8 = group6['Volatility2'].groupby(group6['Date']).mean().reset_index().sort_values(by = 'Volatility2',ascending=False) #use groupby method and get the mean value, then sort such values 
print(res8[0:1],res8[-1:])  #print the first and the last value
'''
        Date  Volatility2
150 2011-08-08     0.073087


        Date  Volatility2
251 2011-12-30     0.014162
'''

## 7.For 2010-2012, for each day of the week, find the average relative volatility for all stocks. 
## (Consider only days when the market is open.)

group7 = df[(df['Date'].dt.year <= 2012) &(df['Date'].dt.year >= 2010)]     #extract the specific time
res9 = group7['Volatility2'].groupby(group7['Date'].dt.dayofweek).mean()    #use groupby method to get the mean of dayofweek
print(res9)     #print the result
'''
Date
0    0.022109
1    0.023836
2    0.023443
3    0.024865
4    0.023018
Name: Volatility2, dtype: float64
'''

## 8.For each month of 2009, determine which stock had the maximum average relative volatility. 
## Give a table with the month (number is fine), stock ticker symbol, and average relative volatility.

group8 = df[df['Date'].dt.year == 2009] #extract the specific time
res10 = group8['Volatility2'].groupby([group8['Date'].dt.month, group8['ticker']]).mean().sort_values(ascending=False)  #use groupby method to get the mean value, then sort such values
res11 = res10.reset_index().groupby(res10.reset_index()['Date']).first()    #reset the index and use groupby method by the data, then extract the first value
print(res11)    #print the result
'''
         Date ticker  Volatility2
                          
1        1    GGP     0.190686
2        2   HBAN     0.275587
3        3    GGP     0.241744
4        4    GGP     0.212291
5        5    GGP     0.187383
6        6    GGP     0.131522
7        7    AIG     0.121527
8        8    AIG     0.141233
9        9    GGP     0.103328
10      10    AAL     0.071610
11      11    GGP     0.089010
12      12    GGP     0.112847
'''

## 9.Find the Open, High, Low, and Close for the Python Index for each day the market was open in 
## January 2013. Give a table the includes the Date, Open, High, Low, and Close, with one date per row.

df['Open2'] = df['Open']*df['Volume']   #create the numerator
df['High2'] = df['High']*df['Volume']   #create the numerator
df['Low2'] = df['Low']*df['Volume'] #create the numerator
df['Close2'] = df['Close']*df['Volume'] #create the numerator
group9 = df[(df['Date'].dt.year == 2013)&(df['Date'].dt.month == 1)][['Date','Open2','High2','Low2','Close2','Volume']] #extract the specific time
res12 = group9.groupby(group9['Date']).sum()    #create the denominator 
for i in res12.columns: #for loop
    res12[i] = res12[i]/res12['Volume'] #let the numerator divided by the denominator and get the python index
print(res12.drop(columns=['Volume']))   #print the result
'''
                Open2      High2       Low2     Close2
Date                                                  
2013-01-02  37.218240  37.669825  36.804244  37.394700
2013-01-03  36.683928  37.175883  36.309854  36.730561
2013-01-04  37.735301  38.197961  37.471489  37.969676
2013-01-07  39.433973  39.952425  39.087880  39.596959
2013-01-08  39.403554  39.748143  38.922081  39.354890
2013-01-09  35.033924  35.411876  34.651302  35.014333
2013-01-10  37.137210  37.527043  36.757483  37.295754
2013-01-11  37.932903  38.256677  37.579063  37.991448
2013-01-14  38.348330  38.759699  37.980530  38.388938
2013-01-15  38.323527  38.880771  38.003460  38.487561
2013-01-16  39.353471  39.731879  38.887220  39.347620
2013-01-17  35.884004  36.233690  35.551895  35.877188
2013-01-18  40.277388  40.652477  39.865453  40.376961
2013-01-22  40.567323  41.068261  40.241281  40.851074
2013-01-23  44.417554  45.121563  44.065735  44.770209
2013-01-24  48.814446  49.728573  48.237470  49.174833
2013-01-25  58.340138  62.089706  58.052795  61.453043
2013-01-28  50.844625  51.450083  49.590466  50.007070
2013-01-29  41.631649  42.499318  41.221507  42.174208
2013-01-30  45.212780  45.587135  44.354852  44.792994
2013-01-31  44.310451  45.061372  43.789490  44.518366
'''

## 10.For the years 2007-2012 determine the top-5 months and years in terms of average relative volatility 
## of the Python Index. Give a table with the month, year, and average relative volatility.

group11 = df[(df['Date'].dt.year >= 2007)&(df['Date'].dt.year <= 2012)][['Date','Open2','High2','Low2','Close2','Volume']]  #extract the specific time
group12 = group11.groupby(group11['Date']).sum()    #create the denominator
for i in group12.columns:   #for loop
    group12[i] = group12[i]/group12['Volume']   #let the numerator divided by denominator to get the python index
group12['Volatility3'] = (group12['High2'] - group12['Low2'])/(0.5*(group12['Open2'] + group12['Close2']))  #use the formula to get the relative volatility of python index
group13 = group12.drop(columns = ['Volume']).reset_index()  #reset index of data
res16 = group13['Volatility3'].groupby([group13['Date'].dt.year,group13['Date'].dt.month]).mean().sort_values(ascending=False)  #use groupby method to get the mean value, then sort such values
print(res16[0:5])   #print the top-5 result

'''
Date  Date
2008  10      0.100923
      11      0.081326
      9       0.067881
2009  3       0.066229
2008  12      0.062545
Name: Volatility3, dtype: float64
'''


