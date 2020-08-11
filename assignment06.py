##
## File: assignment06.py (STAT 3250)
## Topic: Assignment 6
##

##  This assignment requires the data file 'movies.txt'.  This file
##  contains records for nearly 4000 movies, including a movie ID number, 
##  the title (with year of release, which is not part of the title), and a 
##  list of movie genre classifications (such as Romance, Comedy, etc). 

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

import pandas as pd

text = open('movies.txt').read().splitlines()
record = pd.Series(text)

## 1.  Are there any repeated movies in the data set?  A movie is repeated 
##     if the title is exactly repeated and the year is the same.  List any 
##     movies that are repeated, along with the number of times repeated.

title = record.str.split('::').str[1]   #split the string and pick the second part
print(title.value_counts()[title.value_counts() != 1])   #count the value of the same title and print the result

'''
Actually, there are no repeated movies in the data set.
'''

## 2.  Determine the number of movies included in genre "Action", the number
##     in genre "Comedy", and the number in both "Children's" and "Animation".

movie = record.str.split('::').str[2]   #extract the string and pick the third part
Action = len(movie[movie.str.lower().str.contains('action')])   #count the number of movies which contain the action
Comedy = len(record[record.str.contains('Comedy')])   #count the number of movies which contain the comedy
newlines = record[record.str.contains('Animation')]   #count the number of movies which contain the Animation
child = len(newlines[newlines.str.contains('Children')])    #count the number of movies which contain the Children''s

'''
Action: 503
Comedy: 1200
Children's and Animation: 84
'''

## 3.  Among the movies in the genre "Horror", what percentage have the word
##     "massacre" in the title?  What percentage have 'Texas'? (Upper or lower
##     cases are allowed here.) 

group1 = record[record.str.contains('Horror')]  #extract the string which contains Horror
result1 = len(group1[group1.str.lower().str.contains('massacre')])*100/len(group1)  #get the percentage of the string whcih contains massacre
result2 = len(group1[group1.str.lower().str.contains('texas')])*100/len(group1)     #get the percentage of the string which contains texas
print(result1,result2)  #print the result
'''
percentage have word massacre: 2.623906705539359%
percentage have word texas: 1.1661807580174928%
'''

## 4.  How many titles are exactly one word?

title2 = record.str.split('::').str[1].str[:-7].str.split().str.len()   #extract the string and get the title form the string and count the length of the title
result3 = len(title2[title2 == 1])  #judge weather the title is exactly one word
print(result3)

'''
690
'''

## 5.  Among the movies with exactly one genre, determine the top-3 genres in
##     terms of number of movies with that genre.

group3 = record[record.str.split('::').str[-1].str.split('|').str[1].isnull()]  #extract the string the get the catagory and count which one contains only one catagory
result4 = group3.str.split('::').str[-1]    #extract such series and get the catagory
result4.value_counts()[0:3] #get the number of top 3 genres

'''
Drama     843
Comedy    521
Horror    178
dtype: int64
'''

## 6.  Determine the number of movies with 0 genres, with 1 genre, with 2 genres,
##     and so on.  List your results in a table, with the first column the number
##     of genres and the second column the number of movies with that many genres.

movie_genre=record.str.split("::").str[2]  #Get the movie genre.
number = movie_genre.str.split("|").str.len().value_counts().tolist() #count each genres' numbers and list the result in a table
group_df = pd.DataFrame()   #create an empty dataframe
group_df['number of genres'] = [1,2,3,4,5,6]    #set the colume index and its values
group_df['number of movies'] = number      #set the colume index and its values
group_df.append({'number of genres':0, 'number of movies':0},ignore_index=True) #merge such two dataframe and add the extra data with 0 genre

'''
   number of genres  number of movies
0                 1              2025
1                 2              1322
2                 3               421
3                 4               100
4                 5                14
5                 6                 1
6                 0                 0
'''

## 7.  How many remakes are in the data?  A movie is a remake if the title is
##     exactly the same but the year is different. (Count one per remake.  For
##     instance, 'Hamlet' appears 5 times in the data set -- count this as one
##     remake.)

group7 = record.str.split('::').str[1].str.lower().str[:-7]     #extract the string and pick the title
result7 = group7.value_counts()[group7.value_counts() != 1].count() #count the number of title which appears twice or more and count the total number

'''
38
'''

## 8.  List the top-5 most common genres in terms of percentage of movies in
##     the data set.  Give the genre and percentage, from highest to lowest.

group8 = record.str.split('::').str[-1].str.split('|')  #extract the string and pick the third part 
result8 = pd.Series(sum(group8,[])).value_counts()*100/len(record)  #add all genres and count the number, then get the percentage
print(result8[0:5]) #print the top-5 results

'''
Drama       41.282514
Comedy      30.903940
Action      12.953902
Thriller    12.670616
Romance     12.129797
dtype: float64
'''

## 9.  Besides 'and', 'the', 'of', and 'a', what are the 5 most common words  
##     in the titles of movies classified as 'Romance'? (Upper and lower cases
##     should be considered the same.)  Give the number of titles that include
##     each of the words.

group9 = record[record.str.contains('Romance')].str.lower().str.split('::').str[1].str.split('(').str[0].str.split() #extract the string whcih contains romance and pick the title and split by blank
result9 = pd.Series(sum(group9,[])).value_counts()  #count each word and print as a series
print(result9.drop(labels = ['and', 'the', 'of','a'])[0:5]) #drop the for words and get the top 5 words

'''
in      27
love    21
to      14
on      10
you     10
dtype: int64
'''

## 10. It is thought that musicals have become less popular over time.  We 
##     judge that assertion here as follows: Compute the mean release years 
##     for all movies that have genre "Musical", and then do the same for all
##     the other movies.  Then repeat using the median in place of mean.

musical = record[record.str.split('::').str[-1].str.contains('Musical')]    #extrat the string which contains Musical
non_musical = record[~record.str.split('::').str[-1].str.contains('Musical')] #extrat the string which does not contain Musical
musical_year = musical.str.split('::').str[1].str[-6:].str.strip('()')  #extrat the string which contains year
non_musical_year = non_musical.str.split('::').str[1].str[-6:].str.strip('()')  #extrat the string which contains year
musical_year = musical_year.astype(float)   #make the astype method
non_musical_year = non_musical_year.astype(float)   #make the astype method
print(musical_year.mean(),non_musical_year.mean())  #get the mean value of each type
print(musical_year.median(),non_musical_year.median())  #get the median value of each type

'''
the mean of year for movies that have genre "Musical"
1968.7456140350878

the mean of year for movies that do not have genre "Musical"
1986.5908729105863
'''
'''
the median of year for movies that have genre "Musical"
1967.0

the median of year for movies that do not have genre "Musical"
1994.0
'''