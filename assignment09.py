##
## File: assignment09.py (STAT 3250)
## Topic: Assignment 9 
##

##  This assignment requires data from the file 
##
##      'ncaa.csv':  NCAA Men's Tournament Scores, 1985-2019
##
##  The organization of the file is fairly clear.  Each record has information
##  about one game, including the year, the teams, the final score, and each 
##  team's tournament seed.  All questions refer only to the data in this
##  file, not to earlier tournaments.

##  Note: The data set is from Data.World, with the addition of the 2019
##  tournament provided by your dedicated instructor.

## import the package
import pandas as pd

file = pd.read_csv('ncaa.csv')  #read the file

## 1.  Find all schools that have won the championship, and make a table that
##     incluldes the school and number of championships, sorted from most to
##     least.

group1 = file[file['Region Name'].str.contains('Champion')] #extract the frame whic contains champion
test = []   #the empty list
for i in range(len(group1)):    #set the for loop
    if group1.iloc[i]['Score'] > group1.iloc[i]['Score.1']: #if statement to pick the champion
        test.append(group1.iloc[i]['Team']) #append such champion
    else:
        test.append(group1.iloc[i]['Team.1'])   #append such champion
group1['Champion'] = test    #add the champion to the dataframe
print(group1['Champion'].value_counts())    #count the number and print the result
'''
Duke              5
Connecticut       4
North Carolina    4
Kentucky          3
Villanova         3
Florida           2
Louisville        2
Kansas            2
Arizona           1
Arkansas          1
Syracuse          1
Michigan          1
Virginia          1
Indiana           1
UCLA              1
Michigan St       1
Maryland          1
UNLV              1
Name: Champion, dtype: int64
'''

## 2.  Find the top-10 schools based on number of tournament appearances.
##     Make a table that incldes the school name and number of appearances,
##     sorted from most to least.  Include all that tie for 10th position
##     if necessary.

print(sum([],file['Team']).append(sum([],file['Team.1'])).value_counts()[0:10]) #sum all teams and count the number, then print the result
'''
Duke              126
North Carolina    119
Kansas            117
Kentucky          110
Michigan St        87
Arizona            85
Syracuse           81
Louisville         73
Connecticut        71
UCLA               70
dtype: int64
'''

## 3.  Determine the average tournament seed for each school, then make a
##     table with the 10 schools that have the lowest average (hence the
##     best teams). Sort the table from smallest to largest, and include
##     all that tie for 10th position if necessary.

group3 = sum([],file['Seed'].astype(str)).append(sum([],file['Seed.1'].astype(str)))   #sum all seed 
dt3 = pd.DataFrame({'School': sum([],file['Team']).append(sum([],file['Team.1'])),'Seed':group3})   #create the new dataframe which contains the group and seed
res3 = dt3['Seed'].astype(float).groupby(dt3['School']).mean().sort_values()    #use groupby method and get the mean vale of the seed
print(res3[0:10])   #print the top-10 result
'''
School
Duke              1.801587
North Carolina    2.294118
Kansas            2.333333
Kentucky          2.909091
Massachusetts     2.947368
Connecticut       3.309859
Arizona           3.435294
Ohio St           3.537037
Oklahoma          3.822581
UNLV              3.842105
Name: Seed, dtype: float64
'''

## 4.  Give a table of the average margin of victory by round, sorted by
##     round in order 1, 2, ....

file['margin'] = (file['Score'] - file['Score.1']).apply(lambda x: -x if x < 0 else x)  #create the margin column
print(file['margin'].groupby(file['Round']).mean()) #use groupby method and get the mean value, then print the result
'''
Round
1    12.956250
2    11.275000
3     9.917857
4     9.707143
5     9.485714
6     8.257143
Name: margin, dtype: float64
'''

## 5.  Give a table of the percentage of wins by the higher seed by round,
##     sorted by round in order 1, 2, 3, ...

file['Result2'] = ((file['Score'] - file['Score.1'])*(file['Seed'] - file['Seed.1'])).apply(lambda x: 1 if x < 0 else 0)    #create the result2 column, 1 represent win
print(file['Result2'].groupby(file['Round']).sum()/file['Round'].groupby(file['Round']).count() *100)   #use groupby method to get the percentage, then print the result
'''
Round
1    74.285714
2    71.250000
3    71.428571
4    55.000000
5    48.571429
6    57.142857
dtype: float64
'''

## 6.  Determine the average seed for all teams in the Final Four for each
##     year.  Give a table of the top-5 in terms of the lowest average seed
##     (hence teams thought to be better) that includes the year and the
##     average, sorted from smallest to largest.

group6 = file[file['Region Name'].str.contains('Final Four')]   #extract the dataframe which contains final four
group6['Averageseed'] = (group6['Seed']+group6['Seed.1'])/2 #count the average seed
print(group6['Averageseed'].groupby(group6['Year']).mean().sort_values())   #use groupby method to get the mean value, then print the sorted result
'''
Year
2008    1.00
1993    1.25
2007    1.50
2001    1.75
1999    1.75
1997    1.75
1991    1.75
2009    1.75
'''

## 7.  For the first round, determine the percentage of wins by the higher
##     seed for the 1-16 games, for the 2-15 games, ..., for the 8-9 games.
##     Give a table of the above groupings and the percentage, sorted
##     in the order given.

file['ratio'] = file.apply(lambda x:'{s1}-{s2}'.format(s1=x['Seed'], s2=x['Seed.1']),axis = 1)  #create new column which contaisn the ratio
group7 = file[file['Round'] == 1]   #extract the dataframe which only contain the last competition
group7['result'] = group7.apply(lambda x: 1 if x['Score'] - x['Score.1'] > 0 else 0,axis = 1)   #get the result of the final game
print(group7['result'].groupby(group7['ratio']).sum()/group7['ratio'].groupby(group7['ratio']).count()*100) #use groupby method to get the mean value, then print the percentage
'''
ratio
1-16    99.285714
2-15    94.285714
3-14    85.000000
4-13    79.285714
5-12    64.285714
6-11    62.857143
7-10    60.714286
8-9     48.571429
dtype: float64
'''

## 8.  For each champion, determine the average margin of victory in all
##     games played by that team.  Make a table to the top-10 in terms of
##     average margin, sorted from highest to lowest.  Include all that tie
##     for 10th position if necessary.

group8 = pd.merge(group1[['Champion','Year']],file,on = ['Year'])   #merge the original dataframe and the frame which only cobtains the champion
df8 = group8[(group8['Team'] == group8['Champion'])].append(group8[(group8['Team.1'] == group8['Champion'])]).sort_values(by = ['Year'])    #create the dataframe which contains all champion teams
out = pd.merge(group1[['Champion','Year']],df8['margin'].groupby(df8['Year']).mean().reset_index(),on = ['Year'])   #use groupby method and get the mean value, then reset th eindex
print(out.sort_values(by = ['margin'],ascending = False)[0:10]) #sort the value, then print the top-10 result
'''
         Champion  Year     margin
11        Kentucky  1996  21.500000
31       Villanova  2016  20.666667
24  North Carolina  2009  20.166667
5             UNLV  1990  18.666667
33       Villanova  2018  17.666667
16            Duke  2001  16.666667
28      Louisville  2013  16.166667
21         Florida  2006  16.000000
8   North Carolina  1993  15.666667
30            Duke  2015  15.500000
'''

## 9.  For each champion, determine the average seed of all opponents of that
##     team.  Make a table of top-10 in terms of average seed, sorted from 
##     highest to lowest.  Include all that tie for 10th position if necessary.
##     Then make a table of the bottom-10, sorted from lowest to highest.
##     Again include all that tie for 10th position if necessary. 

df8['opponents_seed'] = df8.apply(lambda x: x['Seed'] if x['Score'] < x['Score.1'] else x['Seed.1'],axis = 1)   #create new column which contains seed of all opponents
res8 = pd.merge(group1[['Champion','Year']],df8['opponents_seed'].groupby(df8['Year']).mean().reset_index(),on = ['Year'])   #merge such dataframe and use groupby method to get the mean value, then 
print(res8.sort_values(by = ['opponents_seed'])[0:10],res8.sort_values(by = ['opponents_seed'],ascending = False)[0:11])    #sort the value, then print the result
'''
The top-10:
          Champion  Year  opponents_seed
0        Villanova  1985        3.333333
29     Connecticut  2014        4.666667
31       Villanova  2016        4.833333
8   North Carolina  1993        5.500000
32  North Carolina  2017        5.666667
18        Syracuse  2003        5.666667
24  North Carolina  2009        5.833333
22         Florida  2007        6.000000
11        Kentucky  1996        6.000000
17        Maryland  2002        6.000000
4         Michigan  1989        6.000000

The bottom-10:
         Champion  Year  opponents_seed
5             UNLV  1990        9.000000
28      Louisville  2013        8.500000
34        Virginia  2019        8.000000
23          Kansas  2008        8.000000
21         Florida  2006        7.666667
14     Connecticut  1999        7.500000
1       Louisville  1986        7.500000
9         Arkansas  1994        7.333333
15     Michigan St  2000        7.166667
2          Indiana  1987        7.000000
20  North Carolina  2005        7.000000
'''

## 10. Determine the 2019 champion.

print(group1.iloc[-1]['Champion'])  #print the last result from the champion list
'''
Virginia

UVA! we are the champion
'''