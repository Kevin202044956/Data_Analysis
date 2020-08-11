##
## File: assignment07.py (STAT 3250)
## Topic: Assignment 7 
##

##  This assignment requires data from four files: 
##
##      'movies.txt':  A file of over 3900 movies
##      'users.dat':   A file of over 6000 reviewers who provided ratings
##      'ratings.dat': A file of over 1,000,000 movie ratings
##      'zips.txt':    A file of zip codes and location information
##
##  The file 'readme.txt' has more information about the first three files.
##  You will need to consult the readme file to answer some of the questions.

##  Note: You will need to convert the zip code information in 'users.dat' into
##  state (or territory) information for one or more of the questions below.
##  You must use the information in 'zips.txt' for this purpose, you cannot
##  use other conversion methods. 

import pandas as pd    #import all pacakages we need
import numpy as np

movie = pd.Series(open('movies.txt').read().splitlines())   #read all the files 
rating = pd.Series(open('ratings.dat').read().splitlines()) 
users = pd.Series(open('users.dat').read().splitlines())

users_df = pd.DataFrame({'UserID': users.str.split('::').str[0],
                         'Gender': users.str.split('::').str[1],
                         'Age': users.str.split('::').str[2],
                         'Occupation': users.str.split('::').str[3],
                         'Zipcode': users.str.split('::').str[4].str[0:5]}) # set the user_id to dataframe


group1 = rating.str.split('::')
time = pd.to_datetime(group1.str[3].astype(int),unit = 's')
rating_df = pd.DataFrame({'UserID': group1.str[0],
                          'MovieID': group1.str[1],
                          'Rating': group1.str[2],
                          'Timestamp': time})   #set the rating_df to the dataframe

group2 = movie.str.split('::')
movie_df = pd.DataFrame({'MovieID':group2.str[0],
                         'Title': group2.str[1],
                         'Genres': group2.str[2]})  #set the movie_df to the dataframe


## 1.  Determine the percentage of users that are female.  Do the same for the
##     percentage of users in the 35-44 age group.  In the 18-24 age group,
##     determine the percentage of male users.

fe_per = len(users_df[users_df['Gender'] == 'F'])/len(users_df) *100    #extract the female and calcuate the percentage
group3 = users_df[users_df['Age'] == '35' ] #extract the group which contains 35 age
fe_per2 = len(group3[group3['Gender'] == 'F'])/len(group3) *100     #extract the female and get the percentage
group4 = users_df[users_df['Age'] == '18']  #extract the group which contains 18 age
ma_per = len(group4[group4['Gender'] == 'M'])/len(group4) *100  #extract the male and get the percentage
print(fe_per, fe_per2, ma_per)  #print the result

'''
the percentage of users that are female:
28.294701986754966

the percentage of users in the 35-44 age group:
28.331936295054483

In the 18-24 age group, the percentage of male users
72.98277425203989
'''

## 2.  Give a year-by-year table of counts for the number of ratings, sorted by
##     year in ascending order.

rating_df['year'] = rating_df['Timestamp'].dt.year   #get the datatime and the year
res2 = rating_df.groupby(rating_df['year']).count() #count the year's number
print(res2['Rating'])   #print the rating's number

'''
year
2000    904757
2001     68058
2002     24046
2003      3348
Name: Rating, dtype: int64
'''

## 3.  Determine the average rating for females and the average rating for 
##     males.

merge_df1 = pd.merge(rating_df,users_df)    #merge the dataframe
ave1 = merge_df1[merge_df1['Gender'] == 'F']['Rating'].astype(int).mean()   #extract the female colum and get the mean value
ave2 = merge_df1[merge_df1['Gender'] == 'M']['Rating'].astype(int).mean()   #extract the male colum and get the mean value
print(ave1,ave2)  #print the result

'''
Female: 3.6203660120110372

Male: 3.5688785290984373
'''

## 4.  Find the top-10 movies based on average rating.  (Movies and remakes 
##     should be considered different.)  Give a table with the movie title
##     (including the year) and the average rating, sorted by rating from
##     highest to lowest.  (Include ties as needed.)

merge_df2 = pd.merge(rating_df,movie_df)    #merge such two dataframes
top1 = merge_df2['Rating'].astype(int).groupby(merge_df2['Title']).mean().sort_values(ascending=False)  #use groupbymethod and get the mean value
print(top1[0:10])   #print the top-10 results

'''
Title
Gate of Heavenly Peace, The (1995)           5.0
Lured (1947)                                 5.0
Ulysses (Ulisse) (1954)                      5.0
Smashing Time (1967)                         5.0
Follow the Bitch (1998)                      5.0
Song of Freedom (1936)                       5.0
Bittersweet Motel (2000)                     5.0
Baby, The (1973)                             5.0
One Little Indian (1973)                     5.0
Schlafes Bruder (Brother of Sleep) (1995)    5.0
Name: Rating, dtype: float64
'''

## 5.  Determine the number of movies listed in 'movies.txt' for which there
##     is no rating.  Determine the percentage of these unrated movies for
##     which there is a more recent remake.
        
group5 = movie_df['Title'].append(merge_df2['Title'].drop_duplicates()).drop_duplicates(keep = False)   #get the unrated movie
test_df1 = pd.DataFrame({'Title': movie.str.split('::').str[1].str[:-6].str.strip(),    
                         'Year': movie.str.split('::').str[1].str[-5:-1].str.strip().astype(int)}).reset_index(drop=True)   #split the tital and year
test_df2 = pd.DataFrame({'Title': group5.str[:-6].str.strip(),
                            'Year': group5.str[-5:-1].str.strip().astype(int)}).reset_index(drop=True)  #split the time and the year
test_df3 = test_df1.append(test_df2).drop_duplicates(keep = False)  #get all rated movies
test_df4 = pd.merge(test_df3,test_df2,on='Title')   #merge the rated movies and unrated movies on title
print(len(group5),len(test_df4)/len(test_df1))  #print the result

'''
177

the percentage of these unrated movies for which there is a more recent remake is
0
'''

## 6.  Determine the average rating for each occupation classification 
##     (including 'other or not specified'), and give the results in a
##     table sorted from highest to lowest average and including the
##     occupation title.

res6 = merge_df1['Rating'].astype(int).groupby(merge_df1['Occupation']).mean().sort_values(ascending=False).reset_index() #use groupby method and get the mean value
occu_df = pd.DataFrame({'Occupation': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                        'Title': ["other or not specified","academic/educator","artist","clerical/admin","college/grad student",
                                  "customer service","doctor/health care","executive/managerial","farmer","homemaker","K-12 student",
                                  "lawyer", "programmer","retired","sales/marketing","scientist","self-employed","technician/engineer",
                                  "tradesman/craftsman","unemployed","writer"]})    #input all occupations' title
res7 = res6.astype(float)   #re type the float
res8 = pd.merge(res7,occu_df)   #merge such two dataframes
print(res8) #print the result

'''
    Occupation    Rating                   Title
0         13.0  3.781736                 retired
1         15.0  3.689774               scientist
2          6.0  3.661578      doctor/health care
3          9.0  3.656589               homemaker
4          3.0  3.656516          clerical/admin
5         12.0  3.654001              programmer
6         14.0  3.618481         sales/marketing
7         11.0  3.617371                  lawyer
8         17.0  3.613574     technician/engineer
9          7.0  3.599772    executive/managerial
10        16.0  3.596575           self-employed
11         1.0  3.576642       academic/educator
12         2.0  3.573081                  artist
13         0.0  3.537544  other or not specified
14         5.0  3.537529        customer service
15         4.0  3.536793    college/grad student
16        10.0  3.532675            K-12 student
17        18.0  3.530117     tradesman/craftsman
18        20.0  3.497392                  writer
19         8.0  3.466741                  farmer
20        19.0  3.414050              unemployed
'''



## 7.  Determine the average rating for each genre, and give the results in
##     a table listing genre and average rating in descending order.

df7 = pd.merge(movie_df, rating_df) #merge such two dataframes
array1 = np.concatenate((df7['Rating'].astype(int))*(df7['Genres'].str.split('|'))) #create first array to store all genres time its rating
array2 = np.concatenate(df7['Genres'].str.split('|'))   #create second array to store all genres
res7 = pd.Series(array1).value_counts()/pd.Series(array2).value_counts()    #get the average rating and count values
print(res7.sort_values(ascending=False))    #print the results

'''
Film-Noir      4.075188
Documentary    3.933123
War            3.893327
Drama          3.766332
Crime          3.708679
Animation      3.684868
Mystery        3.668102
Musical        3.665519
Western        3.637770
Romance        3.607465
Thriller       3.570466
Comedy         3.522099
Action         3.491185
Adventure      3.477257
Sci-Fi         3.466521
Fantasy        3.447371
Children's     3.422035
Horror         3.215013
dtype: float64
'''

## 8.  For the user age category, assume that the user has age at the midpoint
##     of the given range.  (For instance '35-44' has age (35+44)/2 = 39.5)
##     For 'under 18' assume an age of 16, and for '56+' assume an age of 60.
##     For each possible rating (1-5) determine the average age of the raters.

#the function which will change age
def func(x):
    if x == '1':
        return 16
    elif x == '18':
        return 21
    elif x == '25':
        return 29.5
    elif x == '35':
        return 39.5
    elif x == '45':
        return 47
    elif x == '50':
        return 52.5
    elif x == '56':
        return 60

test_df = pd.merge(users_df,rating_df)  #merge such two dataframes
test_df['average'] = test_df['Age'].apply(func) #apply such function and change the age
res8 = test_df['average'].groupby(test_df['Rating']).mean() #use groupby method and get the mean value
print(res8) #print the results

'''
Rating
1    31.710783
2    32.769485
3    33.840672
4    34.270909
5    34.368274
Name: average, dtype: float64
'''


## 9.  Find all combinations (if there are any) of occupation and genre for 
##     which there are no ratings.  

group9 = pd.merge(pd.DataFrame(group5),movie_df)    #merge such two dataframes
series = rating_df['MovieID'].drop_duplicates() #get all movieid and drop duplicates
total = 0   #set the index
for i in range(177):    #for loop in all unrated movie
    if group9.loc[i]['MovieID'] in series:  #if the unrated movies' titla appear in the rated movies' series
        total += 1  #the total plus 1
print(total)    #print the result

'''
0
because the movies which there ara no ratings will not appear in the rating dataframe
it is impossiable to find a intersection between movie dataframe and user dataframe,so
there is no combination of occupation and genre for which there are no ratings.
'''


## 10. For each age group, determine the occupation that gave the lowest 
##     average rating.  Give a table that includes the age group, occupation,
##     and average rating.  (Sort by age group from youngest to oldest) 


group10 = test_df['Rating'].astype(int).groupby([test_df['Age'], test_df['Occupation']]).mean() #use groupby method and get the mean value
res10 = pd.DataFrame(group10.sort_values(ascending=True))   #change the result to dataframe and sort the value
print(res10.reset_index().groupby('Age').first())   #reset index and get the first value and print the results

'''
    Occupation    Rating
Age                     
1           11  3.066667
18           6  3.235525
25          19  3.366426
35           8  2.642045
45           4  3.280000
50           8  3.437610
56          14  3.291755
'''

## 11. Find the top-5 states in terms of average rating.  Give in table form
##     including the state and average rating, sorted from highest to lowest.
##     Note: If any of the zip codes in 'users.dat' includes letters, then we
##     classify that user as being from Canada, which we treat as a state for
##     this and the next question.


zips = pd.read_csv('zipcodes.txt', usecols = [1,4],converters={'Zipcode':str}).drop_duplicates()    #extratc the useful data from the zip text file
group11 = pd.merge(zips,merge_df1,on = 'Zipcode')   #merge such two dataframes
res11 = group11['Rating'].astype(int).groupby(group11['State']).mean().sort_values(ascending=False) #use groupby method and get the mean value
print(res11[0:5])   #print the top-5 results

'''
State
GU    4.236842
MS    3.996409
AK    3.985730
AP    3.938967
SC    3.807748
Name: Rating, dtype: float64
'''

## 12. For each genre, determine which state produced the most reviews.  
##     (Include any ties.)

genre_list=[]   #create genre list
movieid_list=[] #create movieid list
for i in movie_df.index:    #for loop
    index=movie_df['Genres'][i].count('|')  #count the numbr of the genres
    for j in range(index+1):    #for the number of the genres
        genre_list.append(movie_df['Genres'][i].split('|')[j])  #genre list will append all genres
        movieid_list.append(movie_df['MovieID'][i]) #movie list will append such movie id
        
movieid_genre=pd.DataFrame({'Genres':genre_list,'MovieID':movieid_list}) #create dataframe to store such two series
temp = pd.merge(zips,users_df,on='Zipcode') #merge such two dataframes
temp2 = pd.merge(temp,rating_df,on='UserID')    #merge such two dataframes
total_df = pd.merge(temp2,movie_df,on= 'MovieID')   #merge such two dataframes and get the total dataframe
res12 = pd.merge(total_df[['MovieID','State']],movieid_genre,on='MovieID')  #merge such two dataframes
res13 = res12['MovieID'].groupby([res12['Genres'],res12['State']]).count().sort_values(ascending=False) #use groupby method and count the total number of each state
print(res13.reset_index(level=['Genres','State']).groupby('Genres').first())    #reset the state and use groupby method to get the first part of each group, then print the results

'''
            State  
Genres                    
Action         CA    46936
Adventure      CA    24149
Animation      CA     7931
Children's     CA    12599
Comedy         CA    63084
Crime          CA    14638
Documentary    CA     1676
Drama          CA    66287
Fantasy        CA     6389
Film-Noir      CA     3662
Horror         CA    12939
Musical        CA     7584
Mystery        CA     7570
Romance        CA    27294
Sci-Fi         CA    28928
Thriller       CA    34583
War            CA    12519
Western        CA     3776

for each state
'''
