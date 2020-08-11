##
## File: exam-solns.py (STAT 3250)
## Topic: Exam 3 Solutions
##

##  Exam 3 consists of three sections.  All code should be submitted as a single 
##  Python file.  Section 3 is on creating plots.  The plots will be submitted 
##  in a separate PDF document.

####
####  Section A
####

##  For this portion of Exam 3 you will be working with Twitter data related
##  to the season opening of Game of Thrones on April 14.  You will use a set
##  of 10,790 tweets for this purpose.  The data is in the file 'GoTtweets.txt'.  
##  The code below can be used to import the data into a list, with each
##  list element a dict of the tweet object.

import json
import pandas as pd
import numpy as np

# Read in the tweets and append them to 'tweetlist'
tweetlist = []
for line in open('GoTtweets.txt', 'r'): # Open the file of tweets
    tweetlist.append(json.loads(line))  # Add to 'tweetlist' after converting
    
df = pd.DataFrame()

## A1. The tweets were downloaded in several groups at about the same time.
##     Are there any that appear in the file more than once?  List the tweet 
##     ID for any repeated tweets, along with the number of times each is
##     repeated.

## Note: For the remaining questions in this section, do not worry about 
##       the duplicate tweets.  Just answer the questions based on the 
##       existing data set.
    
test = np.zeros(len(tweetlist)).astype(str) # create the empty array
for i in range(len(tweetlist)): #for loop 
    test[i] = tweetlist[i]['id_str']    #add the str
df['id'] = test  #set the column
result = df['id'].value_counts()    #count the value
print(result[result>=2])    #print the result
'''
1117619559043948544    2
1117608741099069440    2
1117608744639025152    2
1117619562588057600    2
Name: id, dtype: int64
'''

## A2. Some tweeters like to tweet a lot.  Find the screen name for all 
##     tweeters with at least 5 tweets in the data.  Give the screen name
##     and the number of tweets.  

array2 = np.zeros(len(tweetlist)).astype(str)   #create the empty array
for i in range(len(tweetlist)): #for loop
    array2[i] = tweetlist[i]['user']['screen_name'] #add the screen name to array
df['screen_name'] = array2   #fill the dataframe
result2 = df['screen_name'].value_counts()  #count the value
print(result2[result2 >= 5])    #print the result
'''
Eleo_Ellis         6
taehyungiebtsdm    6
_sherycee          5
caioomartinez      5
Czo18              5
Name: screen_name, dtype: int64
'''

## A3. Determine the number of tweets that include the hashtag '#GoT', then
##     repeat for '#GameofThrones'.
##     Note: Hashtags are not case sensitive, so any of '#GOT', '#got', 'GOt' 
##     etc are all considered matches.  Each tweet object has a list of
##     hashtag objects -- use those for this problem, not the text of the
##     tweet.

Aarray3 = np.zeros(len(tweetlist))  #create the empty array
Aarray4 = np.zeros(len(tweetlist))  #create the empty array
for i in range(len(tweetlist)): #for loop
    for dict in tweetlist[i]['entities']['hashtags']:   #for loop in dict
        if 'got' in dict['text'].lower():   #if statement
            Aarray3[i] = 1  #if ture add 1
        if 'gameofthrones' in dict['text'].lower(): #if statement
            Aarray4[i] = 1  #if ture add 1
print(Aarray3.sum(),Aarray4.sum())  #print the total number
'''
#GoT : 1152.0 

#GameofThrones : 8375.0
'''

## A4. Among the screen names with 4 or more tweets, find the 
##     'followers_count' for each and then give a table of the top-5 
##     (plus ties) in terms of number of followers. Include the screen 
##     name and number of followers.  (If the number of followers changes
##     for a given screen name, then report the average number of followers 
##     among all of the tweeter's tweets.) 

array4 = np.zeros(len(tweetlist))   #create the empty array
for i in range(len(tweetlist)): #for loop
    array4[i] = tweetlist[i]['user']['followers_count']     #store the number of followers
df['followers_count'] = array4   #store the number to the dataframe
a4 = df['followers_count'].groupby(df.screen_name).mean()   #get the mean value
tmp_list = a4.loc[df['screen_name'].value_counts()>=4].sort_values(ascending = False)   #count the value and sort
print(tmp_list[0:5])    #print the top-5 result
'''
screen_name
bbystark          9313.00
Gamoraavengxr     3842.00
Eleo_Ellis        2948.00
HellblazerArts    2506.00
Dahoralu          1901.25
Name: followers_count, dtype: float64
'''

## A5. Find the mean number of hashtags included in the tweets. 

array5 = np.zeros(len(tweetlist))   #create the empty array
for i in range(len(tweetlist)): #set the for loop
    array5[i] = len(tweetlist[i]['entities']['hashtags'])   #store the number of hashtags
print(array5.mean())    #print the mean number
'''
1.0022242817423541
'''

## A6. Give a table of hashtag counts: How many tweets with 0, 1, 2, ...
##     hashtags?

df['hashtag_counts'] = array5   #store the hashtag number
print(df['hashtag_counts'].groupby(df['hashtag_counts']).count())   #use groupby method and count the number
'''
hashtag_counts
0.0     1575
1.0     8111
2.0      768
3.0      242
4.0       55
5.0       24
6.0       10
7.0        2
8.0        1
9.0        1
10.0       1
Name: hashtag_counts, dtype: int64
'''

## A7. Determine the number of tweets that include 'Daenerys' (any combination
##     of upper and lower case) in the text of the tweet.  Then do the same 
##     for 'dragon'.

array7 = np.zeros(len(tweetlist))   #create the empty array
array8 = np.zeros(len(tweetlist))   #create the empty array
for i in range(len(tweetlist)): #set the for loop
    if "daenerys" in tweetlist[i]['text'].lower():  #if statement 
        array7[i] = 1   #if true, add 1
    if "dragon" in tweetlist[i]['text'].lower():    #if statement
        array8[i] = 1   #if true, add 1
print(array7.sum(), array8.sum())   #print the total number
'''
Daenerys : 735.0 

dragon : 385.0
'''

## A8.  Determine the 5 most frequent hashtags, and the number of tweets that
##      each appears in.  As usual, give a table.

array3 = [] #create the empty list
for i in range(len(tweetlist)): #for loop
    for dict in tweetlist[i]['entities']['hashtags']:   #for loop in the dict
        array3.append(dict['text'].lower()) #append the text in lower case
print(pd.Series(array3).value_counts()[0:5])    #count the value and print the top-5 result
'''
gameofthrones           8366
got                     1032
forthethrone             219
gameofthronesseason8     124
demthrones               110
dtype: int64
'''

## A9.  Determine the 5 most frequent 'user_mentions', and the number of tweets 
##      that each appears in.  Give a table.

mention = []    #create the empty list
for i in range(len(tweetlist)): #set the for loop
    for element in tweetlist[i]['entities']['user_mentions']:   #set for loop in methions
        mention.append(element['screen_name'])  #append the screen name
print(pd.Series(mention).value_counts()[0:5])   #count the value and print the top-5 result
'''
GameOfThrones    502
YgorFremo         82
GoTthings_        79
Complex           75
TPAIN             60
dtype: int64
'''

####
####  Section B
####
import glob

filelist = glob.glob('Stocks/*.csv')    #import the file list
df2 = pd.DataFrame() #create a new dataframe
name = []   #create the name list
for f in filelist:  #for loop
    newdf = pd.read_csv(f)  #read csv file
    newdf['ticker'] = f.split('/')[1].split('.')[0] #extract the name from the address
    df2 = pd.concat([df2,newdf])  #concat the dataframe
    name.append(f)  #append the name
    
    
##  We will use the 'Stocks' data sets from Assignment 8 in this section.
##  You can see some information about the data in the assignment description.

##  The time interval covered varies from stock to stock. There are some 
##  missing records, so the data is incomplete. Note that some dates are not 
##  present because the exchange is closed on weekends and holidays. Those 
##  are not missing records. Dates outside the range reported for a given 
##  stock are also not missing records, these are just considered to be 
##  unavailable. Answer the questions below based on the data available in 
##  the files.

## B1.  Use the collective data to determine when the market was open from 
##      January 1, 2008 to December 31, 2015. (Do not use external data for 
##      this question.) Report the number of days the market was open for 
##      each year in 2008-2015. Include the year and the number of days in 
##      table form.

df2['Date'] = pd.to_datetime(df2['Date'])   #create the data time
b1 = pd.DataFrame(df2[(df2['Date'].dt.year >= 2008) &( df2['Date'].dt.year <= 2015)]['Date']).drop_duplicates() #extract the year and drop duplicates
print(b1['Date'].groupby(b1['Date'].dt.year).count())   #use groupby method and count the year
'''
Date
2008    253
2009    252
2010    252
2011    252
2012    250
2013    252
2014    252
2015    252
Name: Date, dtype: int64
'''

## B2.  Determine the total number of missing records for all stocks for the 
##      period 2008-2015.

b2 = pd.DataFrame(df2[(df2['Date'].dt.year >= 2008) &(df2['Date'].dt.year <= 2015)])   #create the dataframe which extract the data
name_list = b2['ticker'].drop_duplicates()  #create the name list
miss = 1    #set the count number
i = 0   #index
miss_array = np.zeros(len(name_list))   #create the array
for name in name_list:  #for loop
    stock_min = b2[b2['ticker'] == name]['Date'].sort_values().iloc[0]  #the first data
    stock_max = b2[b2['ticker'] == name]['Date'].sort_values().iloc[-1] #the second data
    miss_date = len(b1[(b1 >= stock_min)&(b1 <= stock_max)].drop_duplicates(keep = False)) - len(b2[b2['ticker'] == name])  #the number of missing data
    miss_array[i] = miss_date   #create the miss number
    i += 1  # index add 1
    miss += miss_date  #add the missing value
print(miss) #print the result
'''
7168
'''

## B3.  For the period 2008-2015, find the 10 stocks (plus ties) that had the 
##      most missing records, and the 10 stocks (plus ties) with the fewest 
##      missing records. (For the latter, don't include stocks that have no 
##      records for 2008-2015.) Report the stocks and the number of missing 
##      records for each.


missdf = pd.DataFrame({'Name': name_list,'Count': miss_array})  #create the dataframe
print(missdf.sort_values(by = ['Count'],ascending = False)[0:12])   #print the top-10 result
print(missdf.sort_values(by = ['Count'])[0:10]) #print the bottom-10 result

'''
ticker
     Name  Count
124   NBL   44.0
0      RF   37.0
62   HBAN   37.0
0     WAT   36.0
129    LB   36.0
61   PDCO   36.0
81    BBT   36.0
40    SEE   35.0
20   VRSN   35.0
0     RCL   34.0
0     HOT   34.0
61    GAS   34.0

ticker
    Name  Count
0     GM    0.0
0    ZTS    0.0
0    ADT    0.0
0   TRIP    0.0
0   NLSN    0.0
0    XYL    0.0
0    LYB    0.0
0     FB    0.0
0   NWSA    0.0
20  NAVI    0.0
'''

## B4.  Identify the top-10 dates (plus ties) in 2008-2015 that are missing 
##      from the most stocks.  Provide a table with dates and counts.

a = pd.DataFrame()  #create the new dataframe
for name in name_list:  #set the for loop
    stock_min = b2[b2['ticker'] == name]['Date'].sort_values().iloc[0]  #find the first date
    stock_max = b2[b2['ticker'] == name]['Date'].sort_values().iloc[-1] #find the last date
    b = pd.DataFrame(b1[(b1 >= stock_min)&(b1 <= stock_max)].drop_duplicates(keep = False)) #find the missing date
    c= pd.DataFrame(b2[b2['ticker'] == name]['Date'])   #find the total date
    a = pd.concat([b.append(c).drop_duplicates(keep = False),a])    #add the missing date to the dataframe
print(a['Date'].value_counts()[0:23])   #use value count method and print the top-10 result
'''
2012-04-23    11
2013-09-23    10
2011-03-08    10
2013-01-30    10
2013-08-29     9
2009-03-16     9
2013-04-30     9
2010-07-21     9
2008-06-10     9
2011-08-01     9
2013-07-22     9
2009-08-05     9
2008-04-03     9
2012-06-25     9
2008-04-01     9
2012-04-24     9
2009-12-24     9
2009-04-06     9
2013-11-05     9
2009-04-27     9
2009-06-11     9
2012-08-10     9
2009-08-13     9
Name: Date, dtype: int64
'''

##  Questions B5 and B6: For each stock, impute (fill in) the missing records 
##  using linear interpolation. For instance, suppose d1 < d2 < d3 are dates,  
##  and P1 and P3 are known Open prices on dates d1 and d3, respectively, with
##  P2 missing.  Then we estimate P2 (the Open price on date d2) with
##
##       P2 = ((d3 - d2)*P1 + (d2 - d1)*P3)/(d3 - d1)
##
##  The same formula is used for the other missing values of High, Low, Close, 
##  and Volume.  Once you have added the missing records into your data, then
##  use the new data (including the imputed records) to calculate the Python 
##  Index for each date in 2008-2015 (see Assignment 8 for the formula). 
##  Remember that weekends and holidays are not missing records, so don't 
##  impute those.  Once you're done with that, then you can answer B5 and B6.


a = pd.DataFrame()  #create the new dataframe
for name in name_list:  #set the for loop
    stock_min = b2[b2['ticker'] == name]['Date'].sort_values().iloc[0]  #find the first date
    stock_max = b2[b2['ticker'] == name]['Date'].sort_values().iloc[-1] #find the last date
    b = pd.DataFrame(b1[(b1 >= stock_min)&(b1 <= stock_max)].drop_duplicates(keep = False)) #find the missing date
    b['ticker'] = name
    c= pd.DataFrame(b2[b2['ticker'] == name][['Date','ticker']])   #find the total date
    a = pd.concat([b.append(c).drop_duplicates(keep = False),a])
a = a.sort_values(by = ['ticker'])
a = a[~a['Date'].isnull()]

# the array to store number
array_open = np.zeros(len(a))
array_high = np.zeros(len(a))
array_low = np.zeros(len(a))
array_close = np.zeros(len(a))
array_volume = np.zeros(len(a))
#set the for loop
for i in range(len(a)):
    tmp_a = b2[b2['ticker'] == a.iloc[i]['ticker']]
    post_date = tmp_a[tmp_a['Date'] > a.iloc[i]['Date']].iloc[-1]
    previous_date = tmp_a[tmp_a['Date'] < a.iloc[i]['Date']].iloc[0]
    # calculate all missing value
    z1 = (post_date['Date'] - a.iloc[i]['Date']).days * previous_date['Open'] + (a.iloc[i]['Date'] - 
        previous_date['Date']).days *post_date['Open']
    array_open[i] = z1/(post_date['Date'] - previous_date['Date']).days
    z2 = (post_date['Date'] - a.iloc[i]['Date']).days * previous_date['High'] + (a.iloc[i]['Date'] - 
        previous_date['Date']).days *post_date['High']
    array_high[i] = z2/(post_date['Date'] - previous_date['Date']).days
    z3 = (post_date['Date'] - a.iloc[i]['Date']).days * previous_date['Low'] + (a.iloc[i]['Date'] - 
        previous_date['Date']).days *post_date['Low']
    array_low[i] = z3/(post_date['Date'] - previous_date['Date']).days
    z4 = (post_date['Date'] - a.iloc[i]['Date']).days * previous_date['Close'] + (a.iloc[i]['Date'] - 
        previous_date['Date']).days *post_date['Close']
    array_close[i] = z4/(post_date['Date'] - previous_date['Date']).days
    z5 = (post_date['Date'] - a.iloc[i]['Date']).days * previous_date['Volume'] + (a.iloc[i]['Date'] - 
        previous_date['Date']).days *post_date['Volume']
    array_volume[i] = z5/(post_date['Date'] - previous_date['Date']).days
     
#add all missing value
a['Open'] = array_open
a['High'] = array_high
a['Low'] = array_low
a['Close'] = array_close
a['Volume'] = array_volume
finaldf = pd.concat([a,b2])


## B5.  Find the Open, High, Low, and Close for the imputed Python Index for 
##      each day the market was open in January 2013. Give a table the includes 
##      the Date, Open, High, Low, and Close, with one date per row.

dfb5 = finaldf[(finaldf['Date'].dt.year == 2013)&(finaldf['Date'].dt.month == 1)]   #substratc the needed value
dfb5['Open2'] = dfb5['Open']*dfb5['Volume']   #create the numerator
dfb5['High2'] = dfb5['High']*dfb5['Volume']   #create the numerator
dfb5['Low2'] = dfb5['Low']*dfb5['Volume'] #create the numerator
dfb5['Close2'] = dfb5['Close']*dfb5['Volume'] #create the numerator
group9 = dfb5[['Date','Open2','High2','Low2','Close2','Volume']]
res12 = group9.groupby(group9['Date']).sum()    #create the denominator 
for i in res12.columns: #for loop
    res12[i] = res12[i]/res12['Volume'] #let the numerator divided by the denominator and get the python index
print(res12.drop(columns=['Volume']))   #print the result
'''
                Open2      High2       Low2     Close2
Date                                                  
2013-01-02  37.054761  37.505297  36.638862  37.228915
2013-01-03  37.032179  37.523912  36.657750  37.081912
2013-01-04  37.404633  37.863218  37.142403  37.636333
2013-01-07  39.467304  39.985991  39.121514  39.630800
2013-01-08  39.403554  39.748143  38.922081  39.354890
2013-01-09  35.024724  35.401727  34.640686  35.003027
2013-01-10  37.033616  37.421070  36.654474  37.189733
2013-01-11  38.191304  38.514559  37.833823  38.247111
2013-01-14  38.484674  38.900076  38.112640  38.526461
2013-01-15  38.200333  38.754825  37.881484  38.366129
2013-01-16  39.376960  39.755706  38.911310  39.371881
2013-01-17  35.979870  36.329769  35.648391  35.974307
2013-01-18  40.134305  40.504265  39.723440  40.230839
2013-01-22  40.567323  41.068261  40.241281  40.851074
2013-01-23  44.641020  45.344795  44.288949  44.994229
2013-01-24  48.921170  49.827586  48.346726  49.279962
2013-01-25  55.089956  58.565085  54.817362  57.965279
2013-01-28  50.963814  51.568084  49.721003  50.138855
2013-01-29  42.852754  43.719166  42.382627  43.346702
2013-01-30  45.365733  45.742741  44.516468  44.955761
2013-01-31  43.908594  44.645015  43.391417  44.108205
'''

## B6.  Determine the mean Open, High, Low, and Close imputed Python index 
##      for each year in 2008-2015, and report that in a table that includes 
##      the year together with the corresponding Open, High, Low, and Close.

finaldf['Open2'] = finaldf.apply(lambda x: x['Open'] * x['Volume'],axis = 1)    #create the numerator
finaldf['High2'] = finaldf.apply(lambda x: x['High'] * x['Volume'],axis = 1)    #create the numerator
finaldf['Low2'] = finaldf.apply(lambda x: x['Low'] * x['Volume'], axis = 1) #create the numerator
finaldf['Close2'] = finaldf.apply(lambda x: x['Close'] * x['Volume'], axis =1)  #create the numerator
group10 = finaldf[['Date','Open2','High2','Low2','Close2','Volume']]    #extract the dataframe
testb5 = group10[['Open2','High2','Low2','Close2']].groupby(group10['Date'].dt.year).sum()  #get the sum value
testb6 = group10['Volume'].groupby(group10['Date'].dt.year).sum()   #create the denominator 
for i in testb5.columns:    #for loop to get the mean value
    testb5[i] = testb5[i]/testb6
print(testb5)
'''
          Open2      High2       Low2     Close2
Date                                            
2008  38.297877  39.295349  37.183904  38.248995
2009  26.301350  26.889068  25.728390  26.333835
2010  35.297037  35.783507  34.769094  35.292258
2011  38.266909  38.827289  37.633374  38.223187
2012  37.163754  37.653500  36.700465  37.195817
2013  46.799664  47.348290  46.248375  46.810998
2014  57.767802  58.410572  57.074386  57.755198
2015  54.318426  54.962994  53.645172  54.311427
'''

####
####  Section C
####


import matplotlib.pyplot as plot

dfc = pd.read_csv('samplegrades.csv')

##  This section requires the creation of a number of graphs. In addition to 
##  the code in your Python file, you will also upload a PDF document (not Word!)
##  containing your graphs (be sure they are labeled clearly).  The data file 
##  you will use is 'samplegrades.csv'.



## C1.  Make a scatter plot of the 'Math' SAT scores (x-axis) against the 
##      'Read' SAT scores (y-axis). Label the plot 'Math vs Read' and label
##      the axes 'Math' and 'Read'.

#create the plot
plot.scatter(dfc.Math, dfc.Read)
#add label
plot.xlabel('Math')
plot.ylabel('Read')
#add title
plot.title('Math vs Read')
#show
plot.show()

## C2.  Make the same scatter plot as the previous problem, but this time 
##      color-code the points to indicate the 'Sect' and choose different 
##      shapes to indicate the value of 'Prev'.

#create the dataframe which contains all possiable result
c2 = pd.DataFrame({'x1': dfc[(dfc['Sect'] == 'MW200') & (dfc['Prev'] == 'Y')]['Math'],
                    'y1': dfc[(dfc['Sect'] == 'MW200') & (dfc['Prev'] == 'Y')]['Read'],
                    'x2': dfc[(dfc['Sect'] == 'MW200') & (dfc['Prev'] == 'N')]['Math'],
                    'y2': dfc[(dfc['Sect'] == 'MW200') & (dfc['Prev'] == 'N')]['Read'],
                    'x3': dfc[(dfc['Sect'] == 'TR1230') & (dfc['Prev'] == 'Y')]['Math'],
                    'y3': dfc[(dfc['Sect'] == 'TR1230') & (dfc['Prev'] == 'Y')]['Read'],
                    'x4': dfc[(dfc['Sect'] == 'TR1230') & (dfc['Prev'] == 'N')]['Math'],
                    'y4': dfc[(dfc['Sect'] == 'TR1230') & (dfc['Prev'] == 'N')]['Read'],
                    'x5': dfc[(dfc['Sect'] == 'TR930') & (dfc['Prev'] == 'Y')]['Math'],
                    'y5': dfc[(dfc['Sect'] == 'TR930') & (dfc['Prev'] == 'Y')]['Read'],
                    'x6': dfc[(dfc['Sect'] == 'TR930') & (dfc['Prev'] == 'N')]['Math'],
                    'y6': dfc[(dfc['Sect'] == 'TR930') & (dfc['Prev'] == 'N')]['Read']})

#create the plot
plot.scatter(c2.x1,c2.y1, c = 'red', marker = '^')
plot.scatter(c2.x2,c2.y2,c = 'red', marker = 'o')
plot.scatter(c2.x3,c2.y3, c = 'blue', marker = '^')
plot.scatter(c2.x4,c2.y4,c = 'blue', marker = 'o')
plot.scatter(c2.x5,c2.y5, c = 'orange', marker = '^')
plot.scatter(c2.x6,c2.y6,c = 'orange', marker = 'o')
#add label
plot.xlabel('Math')
plot.ylabel('Read')
#add title
plot.title('Math vs Read')
#show
plot.show()

## C3.  Make a histogram of the values of 'CourseAve'. Label the graph 
##      'Course Averages'.

#creat the histogram 
plot.hist(dfc.CourseAve, bins=20)
#add title
plot.title('Course Averages')
#add label
plot.xlabel('Averages score')
plot.ylabel('Count')
#show
plot.show()

## C4.  Make a histogram of the values of 'Final' with color-coded portions 
##      indicating whether they scored at least 75 on the Midterm. Give 
##      the graph appropriate labels.

#extract the needed data
c4y1 = dfc[dfc['Midterm'] >= 75]['Final']
c4y2 = dfc[dfc['Midterm'] < 75]['Final']
#create the histogram
plot.hist((c4y1,c4y2), bins=10, color=['red','blue'])
#add the title
plot.title('Final grade counts')
#add the legend
plot.legend(['Midterm>=75', 'Midterm<75'])
#add the label
plot.xlabel('Final grade')
plot.ylabel('Count')
#show
plot.show()

## C5.  Make a bar chart of the counts for the different values of Year. 
##      Give the graph appropriate labels.

#count the number of year
year = dfc.Year.value_counts().reset_index()
#create the bar picture
plot.bar(year['index'], year['Year'], width=0.5)
#create the title
plot.title('Count by year')
#create the label
plot.xlabel('Year')
plot.ylabel('Count')
#show the picture
plot.show()

## C6.  Make side-by-side box-and-whisker plots for the 'CourseAve' for each 
##      distinct 'Sect'. Give the graph appropriate labels.

#extract the data
data1 = dfc.loc[dfc.Sect == 'MW200'].CourseAve
data2 = dfc.loc[dfc.Sect == 'TR930'].CourseAve
data3 = dfc.loc[dfc.Sect == 'TR1230'].CourseAve
data = [data1,data2,data3]
#create the boxplot
plot.boxplot(data, notch=None, sym='b^')
#add ticks
plot.xticks([1, 2, 3], ['MW200', 'TR930', 'TR1230'])
#add label
plot.xlabel("Section")
plot.ylabel("Course Average (in)")
#add title
plot.title('Course Average by section')
#show the picture
plot.show()




