##
## File: assignment03.py (STAT 3250)
## Topic: Assignment 3
## Name: Kaiwen Zhu(kz8pr)

##  The questions in this assignment refer to the data in the
##  file 'absent.csv'.  The data contains 740 records from an
##  employer, with 21 columns of data for each record.  (There
##  are a few missing values indicated by zeros where zeros 
##  are clearly not appropriate.)  The file 'absent.pdf' has
##  a summary of the meanings for the variables.

##  Questions 1 and 2 can be completed without loops.  You should
##  try to do them this way, grading will take this into account.

## 1.  All questions refer to the data set 'absent.csv'.

import pandas as pd
import numpy as np
import math
record = pd.read_csv('absent.csv')

## 1(a) Find the mean absent time among all records.

mean = np.mean(record)['Absenteeism time in hours']     #find the mean of the absent hours colum
print(mean)     #print the result
'''
the mean absent time is 6.924324324324324
'''
mean = np.mean(record
print(mean)
## 1(b) Determine the number of records corresponding to
##      being absent on a Thursday.

thursday = record.loc[record['Day of the week']==5,['Day of the week']]  #find the the target colum and extract such colum
number1 = thursday.count()  #count the number of element
print(number1)  #print the result
'''
the number of records is 125
'''

## 1(c) Find the number of different employees represented in 
##      this data.

list = []   #create a new list to store the element
different = record['ID'] #extract the id colum
for i in different:  #set a for loop
    if i not in list:  #if statement to determine weather the list has same element
        list.append(i) #if not, append such element
number2 = len(list)  #the number of different employees is the length of list
print(number2)  #print the result
'''
the number of different employees is 36
'''

## 1(d) Find the transportation expense for the employee with
##      ID = 34.

tran = record.loc[record['ID']==34,['Transportation expense']]  #extract the id colum with transportation expense
print(tran.iloc[0]) #print the result by choosing the first row
'''
the transportation expense is 118
'''

## 1(e) Find the mean number of hours absent for the records
##      for employee ID = 11.

absent = record.loc[record['ID'] == 11,['Absenteeism time in hours']]   #extract the target id colum with absencee
mean2 = np.mean(absent)  #find the mean value for the colum
print(mean2)    #print the result
'''
the mean of hours absent is 11.25
'''
## 1(f) Find the mean number of hours absent for the records of those who 
##      have no pets, then do the same for those who have more than one pet.

nopets = record.loc[record['Pet']==0,['Absenteeism time in hours']]   #extract the target no pet colum with absent hours
morepets = record.loc[record['Pet'] > 1,['Absenteeism time in hours']]  #extract the target more than one pets with absent hours
mean3 = np.mean(nopets)   #find the mean value
mean4 = np.mean(morepets)   #find the mean value
print(mean3,mean4)  #print the value
'''
for the people who do not have pet, their mean number of absent hours is 6.828261
for the people who have more than one pet, their mean number of absent hours is 5.21831
'''

## 1(g) Find the percentage of smokers among the records for absences that
##      exceeded 8 hours, then do the same for absences of no more then 4 hours.

totalsmok1 = record.loc[record['Absenteeism time in hours'] > 8,['ID']].count()     #find the total number 
smoknum1 = record.loc[(record['Absenteeism time in hours'] > 8)&(record['Social smoker']==1),['ID']].count()    #find the number of people who smoke in such colum
pent1 = (smoknum1/totalsmok1)*100  #find the percentage
totalsmok2 = record.loc[record['Absenteeism time in hours'] <= 4,['ID']].count()    #find the total number
smoknum2 = record.loc[(record['Absenteeism time in hours'] <= 4)&(record['Social smoker']==1),['ID']].count()   #find the number of people who smoke in such colum
pent2 = (smoknum2/totalsmok2)*100   #find the percentage
print("%" + str(pent1), "%" + str(pent2))   #print the result
'''
the percentage of smokers among the records for absences that exceeds 8 hours is %6.349206
the percentage of smokers among the records for absences that no more than 4 hours is %6.290672
'''

## 1(h) Repeat 1(g), this time for social drinkers in place of smokers.

totaldrink1 = record.loc[record['Absenteeism time in hours'] > 8,['ID']].count()    #find the total number 
drinknum1 = record.loc[(record['Absenteeism time in hours'] > 8)&(record['Social drinker']==1),['ID']].count()  #find the number of people who drink in such colum
pent3 = (drinknum1/totaldrink1)*100  #find the percentage
totaldrink2 = record.loc[record['Absenteeism time in hours'] <= 4,['ID']].count()   #find the total number
drinknum2 = record.loc[(record['Absenteeism time in hours'] <= 4)&(record['Social drinker']==1),['ID']].count() #find the number of people who drink in such colum
pent4 = (drinknum2/totaldrink2)*100  #find the percentage
print("%" + str(pent3), "%" + str(pent4))   #print the result
'''
the percentage of drinkers among the records for absences that exceeds 8 hours is %73.015873
the percentage of drinkers among the records for absences that no more than 4 hours is %53.362256
'''

## 2.  All questions refer to the data set 'absent.csv'.

## 2(a) Find the top-5 employee IDs in terms of total hours absent.  List
##      the IDs and corresponding total hours absent.

groupa = record['Absenteeism time in hours'].groupby(record['ID']) #set a new frame about the absent hour group by ID
resulta = groupa.sum().sort_values(ascending=False) #sort the value from large to small
print(resulta[0:5]) #print the top 5 people
'''
the result is
ID
3     482
14    476
11    450
28    347
34    344
'''

## 2(b) Find the average hours absent per record for each day of the week.
##      Print out the day number and average.

groupb = record['Absenteeism time in hours'].groupby(record['Day of the week']) #set a new frame about the absent hour group by day of week
resultb = groupb.mean() #find the mean value
print(resultb)  #print the result
'''
the result is
Day of the week
2    9.248447
3    7.980519
4    7.147436
5    4.424000
6    5.125000
'''

## 2(c) Repeat 2(b) replacing day of the week with month.

groupc = record['Absenteeism time in hours'].groupby(record['Month of absence']) #set a new frame about the absent hour group by day of week
resultc = groupc.mean() #find the mean value
print(resultc)  #print the result
'''
the result is
Month of absence
0      0.000000
1      4.440000
2      4.083333
3      8.793103
4      9.094340
5      6.250000
6      7.611111
7     10.955224
8      5.333333
9      5.509434
10     4.915493
11     7.507937
12     8.448980
'''

## 2(d) Find the top 3 most common reasons for absence for the social smokers,  
##      then do the same for the non-smokers. (If there is a tie for 3rd place,
##      include all that tied for that position.)

groupd1 = record[record['Social smoker']==1] #creat a new frame about smoker
resultd1 = groupd1['Reason for absence'].groupby(groupd1['Reason for absence']).count().sort_values(  ) #use count method and sort the number
print(resultd1) #print the result
groupd2 = record[record['Social smoker'] == 0]  #creat a new frame about non-smoker
resultd2 = groupd2['Reason for absence'].groupby(groupd2['Reason for absence']).count().sort_values(ascending=False)    #use count method and sort the number
print(resultd2) #print the result
'''
Reason for absence
0     8
25    7
19    4
18    4
28    4
22    4
23    4
the top 3 most common reasons for socical smokers are 25 19 18 28 22 23

Reason for absence
23    145
28    108
27     69
the top 3 most common reasons for non_smokers are 23 28 27
'''

## 2(e) Suppose that we consider our data set as a sample from a much
##      larger population.  Find a 95% confidence interval for the 
##      proportion of the records that are from social drinkers.  Use
##      the formula 
##
##  [phat - 1.96*sqrt(phat*(1-phat)/n), phat + 1.96*sqrt(phat*(1-phat)/n)]
##
## where "phat" is the sample proportion and "n" is the sample size.

groupe1 = record[record['Social drinker'] == 1] #set the new frame about the drinkers
resulte1 = groupe1['ID'].count()        #find the total number of the drinkers
resulte2 = record['ID'].count()     #find the sample size
phat = resulte1/resulte2    #find the p-hat
lowbound = phat - 1.96*math.sqrt(phat*(1-phat)/resulte2)  #find the lower bound of the interval
upbound = phat + 1.96*math.sqrt(phat*(1-phat)/resulte2)  #find the upper bound of the interval
print(lowbound,upbound) #print the result
'''
the 95% confidence interval is [0.5318725067607831,0.603262628374352]
'''

## 3.  For this problem we return to simulations one more time.  Our
##     topic is "bias" of estimators, more specifically the "percentage
##     relative bias" (PRB) which we take to be
##
##        100*((mean of estimated values) - (exact value))/(exact value)
##
##     For instance, to approximate the bias of the sample mean in 
##     estimating the population mean, we would computer
##
##        100*((mean of sample means) - (population mean))/(population mean)
##
##     For estimators that are "unbiased" we expect that the average
##     value of all the estimates will be close to the value of the
##     quantity being estimated.  In these problems we will approximate
##     the degree of bias (or lack of) by simulating.  In all parts we
##     will be sampling from a population of 10,000,000 values randomly
##     generated from an exponential distribution with scale = 10 using
##     the code below.

pop = np.random.exponential(scale = 10, size = 10000000)

## 3(a) Compute and report the mean for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample mean for each of the samples,
##      compute the mean of the sample means, and then compute the PRB.

popmean = np.mean(pop) #set the population mean
totala = 0 #set the total mean
for i in range(100000): #set the for loop for 100000 times
    samp = np.random.exponential(scale = 10,size = 10)  #set the sample distribution
    totala += np.mean(samp)   #find the mean of each sample and add them together
sampmean = totala/100000   #find the sample mean
PRBa = 100*(sampmean - popmean)/popmean    #find the bias by using the fomula
print(str(PRBa)+ '%')  #print the result
print(sampmean)     #print the sample mean
print(popmean)  #print the population mean
'''
my population mean is 9.999021309372498
my sample mean is 10.009050338962432
and my percentage relative bias is 0.10030011217730711%
'''

## 3(b) Compute and report the variance for all of "pop" using "np.var(pop)".  
##      Simulate 100,000 samples of size 10, then compute the sample variance 
##      for each sample using "np.var(samp)" (where "samp" = sample).  Compute 
##      the mean of the sample variances, and then compute the PRB.
##      Note: Here we are using the population variance formula on the samples
##      in order to estimate the population variance.  This should produce
##      bias, so expect something nonzero for the PRB.

popvar = np.var(pop)    #set the population varience
totalb = 0  #set the total varience
for i in range(100000):    #set the for loop for 100000 times
    samp2 = np.random.exponential(scale = 10,size = 10)  #set the sample distribution
    totalb += np.var(samp2)  #find the varience of each sample and add them together
sampvar = totalb/100000     #find the samp varience
PRBb = 100*(sampvar-popvar)/popvar    #find the bias by using the fomula
print(str(PRBb) + '%') #print the result
print(sampvar)  #print the sample varience
print(popvar)   #print the population varience
'''
my population mean is 99.98941170963822
my sample varience is 90.08512435666464
and my percentage relative bias is -9.90533615872738%
'''

## 3(c) Repeat 3(b), but this time use "np.var(samp, ddof=1)" to compute the
##      sample variances.  (Don't change "np.var(pop)" when computing the
##      population variance.)

popvar = np.var(pop)    #set the population varience
totalc = 0  #set the total varience
for i in range(100000):    #set the for loop for 100000 times
    samp3 = np.random.exponential(scale = 10,size = 10)  #set the sample distribution
    totalc += np.var(samp3,ddof=1)  #find the varience of each sample and add them together
sampvar2 = totalc/100000     #find the sample varience
PRBc = 100*(sampvar2-popvar)/popvar    #find the bias by using the fomula
print(str(PRBc)+ '%') #print the result
print(sampvar2) #print the sample varience
print(popvar)   #print the population varience
'''
my population mean is 99.98941170963822
my sample varience is 99.57313889975292
and my percentage relative bias is -0.41631689072651473%
'''

## 3(d) Compute and report the median for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample median for each of the samples,
##      compute the mean of the sample medians, and then compute the PRB.
##      Note: For nonsymmetric distributions (such as the exponential) the
##      sample median is a biased estimator for the population median.  The
##      bias gets decreases with larger samples, but should be evident with 
##      samples of size 10.

popmedian = np.median(pop)  #set the population median
totald = 0      #set the total median
for i in range(100000):
    samp4 = np.random.exponential(scale = 10,size = 10)  #set the sample distribution
    totald += np.median(samp4)  #find the median of each sample and add them together
sampmedian = totald/100000      #find the sample median
PRBd = 100*(sampmedian - popmedian)/popmedian   #get the bias by using the fomula
print(str(PRBd)+ '%')   #print the bias result
print(sampmedian)   ##print the sample median
print(popmedian)   #print the population median
'''
my population median is 6.930031903224485
my sample median is 7.467245583098807
and my percentage relative bias is 7.349519774023127%
'''

