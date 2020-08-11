##
## File: assignment02.py (STAT 3250)
## Topic: Assignment 2
##
import numpy as np 
## 1.
##
## 1(a) Generate an array x of 10000 random values from 
##      a uniform distribution on the interval [0,50],
##      then use a for loop to determine the percentage     
##      of values that are in the interval [8,27].

## Note: 1(a) asks for a percentage, not a count and not
##       a proportion.

number1 = 0  # record the number of values
arrx = np.array(np.random.uniform(low = 0, high = 50, size = 10000))  # create the array
for element in arrx:  # define the for loop
    if 8 <= element <= 27:  #set the jugement statement
        number1 += 1        #if true, the count should be plused one
result1 = (number1/10000)*100   #calculate the result
print(str(result1)+"%") #print the result
'''
the percentage is almost 37.91%
'''
## 1(b) Repeat 1(a) 1000 times, then compute the average
##      of the 1000 percentages found.

totalcases = 1000*10000     #record totalcases
number2 = 0     # record the number of values
for i in range(1000):   #define the for loop
    arrx2 = np.array(np.random.uniform(low = 0, high = 50, size = 10000))   # create the array
    for element in arrx2:  # define the for loop
        if 8 <= element <= 27:  #set the jugement statement
            number2 += 1        #if true, the count should be plused one
result2 = (number2/totalcases)*100   #calculate the result
print(str(result2)+"%")    #print the result
'''
the average percentage is almost 37.99776%
'''

## 1(c) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      first that is less than 3.

number3 = 1     ##record the number
index = np.random.randint(low = 0,high = 10000)  #set the index form 0 to 10000
element = arrx[index]  #pick randomly from the arrx
while element >= 3:     #set the while loop
    index = np.random.randint(low = 0,high = 10000) #recreat a new index
    element = arrx[index]   #repick the new element 
    number3 += 1    #when element is bigger than 3, plus 1
print(number3)  #print the result
'''
the result is 11
'''

## 1(d) Repeat 1(c) 1000 times, then compute the average for the
##      number of random entries required.

number4 = 1     ##record the number
for i in range(1000): #set a for loop 1000 times
    index2 = np.random.randint(low = 0,high = 10000)  #set the index form 0 to 10000
    element2 = arrx[index2]  #pick randomly from the arrx
    while element2 >= 3:     #set the while loop
        index2 = np.random.randint(low = 0,high = 10000) #recreat a new index
        element2 = arrx[index2]   #repick the new element 
        number4 += 1    #when element is bigger than 3, plus 1
result4 = number4/1000  #calculate the result
print(result4)  #print the result
'''
the average number is almost 15.845
'''

## 1(e) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      third entry that exceeds 36.


number5 = 0     #record the number
ct2 = []        #create the list to store the element
while True:     #set the while loop
    index5 = np.random.randint(low = 0,high = 10000) #creat a new index
    element5 = arrx[index5]   #pick the new element
    if element5 > 36:   #if statement to determine weather element is greater than 36
            ct2.append(element5)    ##if true, put the element into the count list
    number5 += 1     #when element is less than 36, plus 1
    if len(ct2) == 3:   ##if statement to determine weather find the third element 
        break    #if true, break the loop
    number5 += 1    #when element is less than 36, plus 1
print(number5) #print the result
'''
the number to find the third entry that exceeds 36 is 13
'''

## 1(f) Repeat 1(e) 5000 times, then compute the average for the
##      number of random entries required.

number6 = 0     #record the number
for i in range(5000):       #set the for loop for 5000 times
    ct = []      #set the count list
    while True:     #set the while loop
        index6 = np.random.randint(low = 0,high = 10000) #creat a new index
        element6 = arrx[index6]   #pick the new element
        if element6 > 36:    #if statement to determine weather element is greater than 36
            ct.append(element6) #if true, put the element into the count list
        number6 += 1     #when element is less than 36, plus 1
        if len(ct) == 3:    #if statement to determine weather find the third element 
            break   #if true, break the loop
result6 = number6/5000   #calculate the result
print(result6)  #print the result
'''
the average number to find the third entry that exceeds 36 is 10.5232
'''

## 2.   For this problem you will draw samples from a normal
##      population with mean 40 and standard deviation 12.
##      Run the code below to generate your population, which
##      will consist of 1,000,000 elements.

import numpy as np 
p1 = np.random.normal(40,12,size=1000000)

## 2(a) The formula for a 95% confidence interval for the 
##      population mean is given by
##     
##      [xbar - 1.96*sigma/sqrt(n), xbar + 1.96*sigma/sqrt(n)]
##
##      where xbar is the sample mean, sigma is the population
##      standard deviation, and n is the sample size.
##
##      Select 10,000 random samples of size 10 from p1.  For
##      each sample, find the corresponding confidence 
##      interval, and then determine the percentage of
##      confidence intervals that contain the population mean.
##      (This is an estimate of the confidence level.)

number7 = 0   #record the number
for i in range(10000):  #set the for loop for 10000 times
    total = 0       #record the total value in the sample
    samp1 = np.random.choice(p1,size = 10)      #randomly choice with size 10
    for element in samp1:       #for loop to get total value
        total += element  #find the total value
    mean1 = total/10    #the sample mean
    if (mean1 - 23.52/(10**(1/2))) <= 40 <= (mean1 + 23.52/(10**(1/2))):    #jugement statement
        number7 += 1    #if true, the number will be plused 1
result7 = (number7/10000)*100   # calculate the result
print(str(result7)+"%")   #print the result
'''
the confidence level is almost 95.03%
'''

## 2(b) Frequently in applications the population standard
##      deviation is not known. In such cases, the sample
##      standard deviation is used instead.  Repeat part 2(a)
##      replacing the population standard deviation with the
##      standard deviation from each sample, so that the
##      formula is
##
##      [xbar - 1.96*stdev/sqrt(n), xbar + 1.96*stdev/sqrt(n)]
##
##      Tip: Recall the command for the standard deviation is 
##           np.std(data, ddof=1)

number8 = 0   #record the number
for i in range(10000):      #set the for loop for 10000 times
    total2 = 0       #record the total value in the sample
    samp2 = np.random.choice(p1,size = 10)      #randomly choice with size 10
    for element in samp2:       #for loop to get total value
        total2 += element     #find the total value
    mean2 = total2/10  #the sample mean
    std2 = np.std(samp2,ddof = 1)   #get the sample standard deviation
    if (mean2 - 1.96*std2/(10**(1/2))) <= 40 <= (mean2 + 1.96*std2/(10**(1/2))): #jugement statement
        number8 += 1    #if true, the number will be plused 1
result8 = (number8/10000)*100   # calculate the result
print(str(result8)+"%")   #print the result
'''
the confidence level is almost 91.96%
'''

## 2(c) Your answer in part 2(b) should be a bit off, in that
##      the estimated confidence level isn't quite 95%.  The 
##      problem is that a t-distribution is appropriate when
##      using the sample standard deviation.  Repeat part 2(b),
##      this time using t* in place of 1.96 in the formula,
##      where: t* = 2.262 for n = 10.

number9 = 0     #record the number
for i in range(10000):      #set the for loop for 10000 times
    total3 = 0       #record the total value in the sample
    samp3 = np.random.choice(p1,size = 10)      #randomly choice with size 10
    for element in samp3:       #for loop to get total value
        total3 += element
    mean3 = total3/10   #the sample mean
    std3 = np.std(samp3,ddof = 1)   #get the sample standard deviation
    if (mean3 - 2.262*std3/(10**(1/2))) <= 40 <= (mean3 + 2.262*std3/(10**(1/2))):  #jugement statement
        number9 += 1    #if true, the number will be plused 1
result9 = (number9/10000)*100   # calculate the result
print(str(result9)+"%")   #print the result
'''
the confidence level is almost 95.15%
'''

## 3.   Suppose that random numbers are selected one at a time
##      with replacement from among the set 0, 1, 2, ..., 8, 9.
##      Use 10,000 simulations to estimate the average number 
##      of values required to select three identical values in 
##      a row.

number10 = 1    #record the number
pop = [0,1,2,3,4,5,6,7,8,9]     #create the sample 
for i in range(10000):  #set for loop for 10000 times
    j = 0       #create a j index 
    testlist = [None,None]   #create a list with two None elements
    while True:     #the while loop
        randomnumber = np.random.choice(pop,size=1)     #randomly pick a number from sample
        testlist.append(randomnumber)   #put the number into the list
        number10 += 1   #number will be plused 1 if we do not have three same elements
        if  testlist[j] == testlist[j+1] == testlist[j+2]:  #compare three elements in a row
            break   #if the number is 3, break the while loop
        j += 1   #the j index plus one
result10 = number10/10000   #calculate the average result
print(result10)     #print the result
'''
the average number to select three identical value in a row is almost 111.7132
'''

## 4.   Jay is taking a 20 question true/false quiz online.  The
##      quiz is configured to tell him whether he gets a question
##      correct before proceeding to the next question.  The 
##      responses influence Jay's confidence level and hence his 
##      exam performance.  In this problem we will use simulation
##      to estimate Jay's average score based on a simple model.
##      We make the following assumptions:
##    
##      * At the start of the quiz there is a 80% chance that 
##        Jay will answer the first question correctly.
##      * For all questions after the first one, if Jay got 
##        the previous question correct, then there is a
##        88% chance that he will get the next question
##        correct.  (And a 12% chance he gets it wrong.)
##      * For all questions after the first one, if Jay got
##        the previous question wrong, then there is a
##        70% chance that he will get the next question
##        correct.  (And a 30% chance he gets it wrong.)
##      * Each question is worth 5 points.
##
##      Use 10,000 simulated quizzes to estimate the average 
##      score.

number11 = 0        #set the total number of total correct questions
for i in range(10000):      #set for loop for 10000 times
    answer = np.random.choice([0,1], size=1, p=[0.2,0.8])   #pick the answer at the first question
    for i in range(20):     #set the for loop for 20 times
        if answer == 1:     #if answer is correct
            answer = np.random.choice([0,1], size=1, p=[0.12,0.88])     #following the correct probability distribution
            number11 += 1   #the number of correct answer plus one
        else:   #if false
            answer = np.random.choice([0,1], size=1, p=[0.3,0.7])   #following the wrong probability distribution
averagescore = (number11*5)/10000   #get the average score of the quiz
print(averagescore)     #print the result
'''
the average score will be 85.0995
'''

## 5.   The questions in this problem should be done without the 
##      use of loops.  They can be done with NumPy functions.
##      The different parts use the array defined below.

import numpy as np # Load NumPy
arr1 = np.array([[2,5,7,0,2,5,-6,8,1,-9],[-1,3,4,2,0,1,3,2,1,-1],
                [3,0,-2,-2,5,4,5,9,0,7],[1,3,2,0,4,5,1,9,8,6],
                [1,1,0,1,5,3,2,9,0,-9],[0,1,7,7,7,-4,0,2,5,-9]])

## 5(a) Extract a submatrix arr1_slice1 from arr1 that consists of
##      the second and third rows of arr1.

arr1_slice1 = np.copy(arr1[[1,2]])  #extract a submatrix form the arr1 which consist of the second and third row
print(arr1_slice1)
'''
the sublist from arr1 is 
[[-1  3  4  2  0  1  3  2  1 -1]
 [ 3  0 -2 -2  5  4  5  9  0  7]]
'''
    
## 5(b) Find a one-dimensional array that contains the entries of
##      arr1 that are less than -2.

mylist = []     #create a list
for row in arr1:  #for the rwo in arr1
    for element in row:  #for the element in such row
        if element < -2:  #if statement
            mylist.append(element) #append such element into the list
newarray = np.array(mylist) #create a new array
print(newarray) #print the result
'''
the array which contains the entries of arr1 that are less than -2 is
[-6 -9 -9 -4 -9]
'''

## 5(c) Determine the number of entries of arr1 that are greater
##      than 4.

number12 = 0 #set the number of entries
for row in (arr1 > 4):  #set the for loop for the boolean result
    for element in row:  #for each element in such row
        if element:  #if statement
            number12 += 1  #if true, the number12 will be plused 1
print(number12) #print the result
'''
the number of entries of arr1 that are greater than 4 is 18
'''

## 5(d) Find the mean of the entries of arr1 that are less than
##      or equal to -2.

arr1mean = np.mean(arr1[arr1<=-2]) #the mean of the entries of arr1 that are less than or equal to -2
print(arr1mean) #print the result
'''
the mean of entries of arr1 which are less than or equal to -2 is 
-5.857142857142857
'''

## 5(e) Find the sum of the squares of the odd entries of arr1.
##      (Note: This is the entries that are odd numbers, not the
##       entries indexed by odd numbers.)

number13 = 0  #set the total value
newarray2 = np.where(arr1 % 2 == 0, 0, arr1)  #replace all even entries with 0
for row in newarray2:  #for the rwo in newarray2
    for element in row:  #for the element in such row
        number13 += element**2 #the sum of the squares of the odd entries
print(number13) #print the result
'''
the sum of the squares of the odd entries of arr1 is 962
'''
        
## 5(f) Determine the proportion of positive entries of arr1 
##      that are greater than 5.

number14 = (np.size(arr1[arr1 > 5]))/np.size(arr1[arr1>0])  #the proportion of positive entries of arr1 that are greater than 5.
print(number14) #print the result
'''
the proportion of positive entries of arr1 that are greater than 5 is 
0.2619047619047619
'''












