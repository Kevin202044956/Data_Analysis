##
## File: assignment04.py (STAT 3250)
## Topic: Assignment 4
## Name: Kaiwen Zhu(kz8pr)

##  This assignment requires the data file 'airline_tweets.csv'.  This file
##  contains records of over 14000 tweets and associated information related
##  to a number of airlines.  You should be able to read this file in using
##  the usual pandas methods.

##  Note: Questions 1-9 should be done without the use of loops.  
##        Questions 10-13 can be done with loops.

import pandas as pd
record = pd.read_csv('airline_tweets.csv')

## 1.  Determine the number of tweets for each airline, indicated by the
##     name in the 'airline' column of the data set.  Give the airline 
##     name and number of tweets in table form.

group1 = record['tweet_id'].groupby(record['airline']).count()  #set the dataframe and use the groupby and count method 
print(group1)   #print the result
'''
airline
American          2759
JetBlue           2222
Southwest         2420
US Airways        2913
United            3822
Virgin America     504
'''

## 2.  For each airlines tweets, determine the percentage that are positive,
##     based on the classification in 'airline_sentiment'.  Give a table of
##     airline name and percentage, sorted from largest percentage to smallest.

group2 = record[record['airline_sentiment'] == 'positive'] #count the data whose airline sentiment is positive
group3 = group2['tweet_id'].groupby(group2['airline']).count()   #group such dataframe and count the number
result1 = (group3*100/group1).sort_values(ascending=False)  #calulate the percentage and print the result
print(result1)
pd.
'''
airline
Virgin America    30.158730%
JetBlue           24.482448%
Southwest         23.553719%
United            12.872841%
American          12.178325%
US Airways         9.234466%
'''

## 3.  List all user names (in the 'name' column) with at least 20 tweets
##     along with the number of tweets for each.  Give the results in table
##     form sorted from most to least.

group4 = record['unit_id'].groupby(record['name']).count().sort_values(ascending=False) #set the new dataframe groupby the name and count the number
result2 = group4[group4 >= 20]  #substract the number which is greater than 20
print(result2)  #print the result
'''
name
JetBlueNews        63
kbosspotter        32
_mhertz            29
otisday            28
throthra           27
weezerandburnie    23
rossj987           23
GREATNESSEOA       22
MeeestarCoke       22
scoobydoo9749      21
jasemccarty        20
'''

## 4.  Determine the percentage of tweets from users who have more than one
##     tweet in this data set.

group5 = group4[group4 > 1].sum() #extract the dataframe which has more than 1 tweet
result3 = group5/group4.sum()*100   #calculate the percentage
print(result3)  #print the result
'''
the percentage is 67.88934426229508%
'''

## 5.  Among the negative tweets, which five reasons are the most common?
##     Give the percentage of negative tweets with each of the five most 
##     common reasons.  Sort from most to least common.

group6 = record[record['airline_sentiment'] == 'negative']  #create a new dataframe which sentiment is negative
result4 = group6['airline_sentiment'].groupby(group6['negativereason']).count().sort_values(ascending=False)*100/group6['airline_sentiment'].count()# calculate such percentage and sort the value
print(result4[0:5] + '%') #print the top 5 results
'''
negativereason
Customer Service Issue    31.706254%
Late Flight               18.141207%
Can't Tell                12.965788%
Cancelled Flight           9.228590%
Lost Luggage               7.888429%
'''
## 6.  How many of the tweets for each airline include the phrase "on fleek"?

group7 = record[record['text'].str.contains('on fleek')]    #create a datagrame which text contains on fleek
result5 = group7['tweet_id'].groupby(group7['airline']).count() #count the number
print(result5)  #print the result
'''
airline
JetBlue           146
Virgin American    0
United             0
Southwest          0
US Airways         0
American           0
'''

## 7.  What percentage of tweets included a hashtag?

group8 = record[record['text'].str.contains('#')]   #extract the dataframe whose text contains hashtag
result6 = len(group8)*100/len(record)   #calculate the percentage
print(result6)  #print the result
'''
the percentage is 17.00136612021858%
'''

## 8.  How many tweets include a link to a web site?

group9 = record[record['text'].str.contains('http')]    #extract the dataframe whoes text contains website
print(len(group9))  #print the number of such dataframe
'''
the number is 1173
'''

## 9.  How many of the tweets include an '@' for another user besides the
##     intended airline?

group10 = record[record['text'].str.count('@') >= 2]
print(len(group10)) #print the result
'''
the number is 1645
'''

## 10. Suppose that a score of 1 is assigned to each positive tweet, 0 to
##     each neutral tweet, and -1 to each negative tweet.  Determine the
##     mean score for each airline, and give the results in table form with
##     airlines and mean scores, sorted from highest to lowest.

record['score'] = ''     #create a new colume to record the number
for i in range(len(record)):    #set the for loop
    if record.loc[i,'airline_sentiment'] == 'positive': #if the airline_sentiment is postive, record 1
        record.loc[i,'score'] = 1       #record 1
    elif record.loc[i,'airline_sentiment'] == 'negative':   #if the airline_sentiment is negative, record -1
        record.loc[i,'score'] = -1  #record -1
    elif record.loc[i,'airline_sentiment'] == 'neutral':    #if the airline_sentiment is netural, record 0
        record.loc[i,'score'] = 0   #record 0
result7 = record['score'].groupby(record['airline']).mean().sort_values(ascending=False)    #find the mean value and sort the value from large to small
print(result7)  #print the result
'''
airline
Virgin America   -0.057540
JetBlue          -0.184968
Southwest        -0.254545
United           -0.560178
American         -0.588619
US Airways       -0.684518
'''

## 11. Among the tweets that "@" a user besides the indicated airline, 
##     what percentage include an "@" directed at the other airlines 
##     in this file? (Note: Twitterusernames are not case sensitive, 
##     so '@MyName' is the same as '@MYNAME' which is the same as '@myname'.)
    
    
total = 0   #set the total number
for i in range(len(record)):    #set the for loop
    samp =['@virginamerica','@united','@southwestair','@jetblue','@usairways','@americanair']   #def a sample which has all indicated airline
    num = 0 #set a number to record the apperaing times of each airline
    string = record.loc[i,'text'].lower().strip().split(' ')    #set the string with lower case and split by space
    for element in string:  #for each words in such string
        if element in samp: #if such airline appear in the sample
            samp.remove(element)    #remove such airline
            num += 1    #record this removement
            if num == 2:    #if the element is the second other airline
                total += 1  #the total number will be added one
                break #break such loop
percentage = total*100/len(group10) #the result will be the total number divided by the answer from question 9
print(percentage)   #print the result

'''
the percentage is 18.72340425531915%
'''

## 12. Suppose the same user has two or more tweets in a row, based on how they 
##     appear in the file. For such tweet sequences, determine the percentage
##     for which the most recent tweet (which comes nearest the top of the
##     file) is a positive tweet.
 
newrecord = record.copy()   #create a new copy record
newrecord['secret'] = ''    #create a new colume to record the number
i = -1  #set the start index
while True: #while loop
    n = 1   #the record number start from 1
    i += 1  #the index will be added 1
    while newrecord.loc[i,'name'] == newrecord.loc[i+1, 'name']:    #if the first name equals to the second name
        newrecord.loc[i,'secret'] = n    #record the first name n
        newrecord.loc[i+1,'secret'] = n+1   #record the second name n+1
        n += 1  #the number will be added 1
        i += 1  #the index will be added 1 to compare the next pair of names
    if i == 14638:  #if the while loop has compared all pairs
        break    #break the loop
newgroup = newrecord[newrecord['secret'] == 1]  #the dominator will be the number of first name
newgroup2 = newgroup[newgroup['airline_sentiment'] == 'positive']   #get the number of the first name which has positive
result10 = len(newgroup2)*100/len(newgroup) #get the percentage
print(result10)   #print the result
'''
the percentage is 11.189634864546525%
'''
        
## 13. Give a count for the top-10 hashtags (and ties) in terms of the number 
##     of times each appears.  Give the hashtags and counts in a table
##     sorted from most frequent to least frequent.  (Note: Twitter hashtags
##     are not case sensitive, so '#HashTag', '#HASHtag' and '#hashtag' are
##     all regarded as the same. Also ignore instances of hashtags that are
##     alone with no other characters.)

list2 = []  #create a new list to append elements
for i in range(len(record)):    #set the for loop
    string = record.loc[i,'text'].lower().strip().split(' ')    #create the string list from the text with lower case
    for element in string:  #for each element in such string list
        if '#' in element and element != '#':   #if the element has '#' and is not just '#'
            list2.append(element)   #append such element in the initial list
df = pd.Series(list2)   #make the list be a dataframe
result11 = df.value_counts()    #count each value
print(result11[0:10])   #print the top 10 result
'''
the rsult is

#destinationdragons    76
#fail                  64
#jetblue               44
#unitedairlines        43
#customerservice       34
#usairways             30
#usairwaysfail         26
#neveragain            26
#americanairlines      25
#united                25
'''
    







