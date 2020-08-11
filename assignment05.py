##
## File: assignment05.py (STAT 3250)
## Topic: Assignment 5
## Name: Kaiwen zhu(kz8pr)

##  This assignment requires the data file 'diabetic_data.csv'.  This file
##  contains records for over 100,000 hospitalizations for people who have
##  diabetes.  The file 'diabetic_info.csv' contains information on the
##  codes used for a few of the entries.  Missing values are indicated by
##  a '?'.  You should be able to read in this file using the usual 
##  pandas methods.

import pandas as pd
import numpy as np
import re
info = pd.read_csv('diabetic_info.csv')
record = pd.read_csv('diabetic_data.csv')
##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

## 1.  Determine the average number of medications ('num_medications') for 
##     males and for females.

group1 = record[record['gender'] == 'Male'] #extract the group1 which only contains male
result1 = group1['num_medications'].sum()/len(group1)   #find the sum and divided by number
group2 = record[record['gender'] == 'Female']   #extract the group2 which only contains female
result2 = group2['num_medications'].sum()/len(group2)   #find the sum and divided by total number
print('male:' + str(result1)+ '  female: ' + str(result2))  #print the result
'''
the average number is:
male:15.828774837955583  female: 16.187888425824376
'''

## 2.  Determine the average length of hospital stay ('time_in_hospital')
##     for each race classification.  (Omit those unknown '?' but include 
##     those classified as 'Other'.)

group3 = record['time_in_hospital'].groupby(record['race']).mean()  #extract the groups which has time_in_hospital group by race
print(group3)   #print the result
'''
race
AfricanAmerican    4.507860
Asian              3.995320
Caucasian          4.385721
Hispanic           4.059892
Other              4.273572
(the result has omitted the unknown '?')
'''

## 3.  Among males, find a 95% confidence interval for the proportion that 
##     had at 2 or more procedures ('num_procedures').  Then do the same 
##     for females.

group4 = record[record['gender'] == 'Male']    #extract the male dataframe 
p_hat1 = len(record.loc[(record['num_procedures'] >=2) & (record['gender'] == 'Male')])/len(group4) #get the percentage which procedures is greater than 2
lb1 = p_hat1 - 1.96 * np.sqrt(p_hat1 * (1 - p_hat1) / len(group4))  #get the lower bound 
rb1 = p_hat1 + 1.96 * np.sqrt(p_hat1 * (1 - p_hat1) / len(group4))  #get the upper bound
group5 = record[record['gender'] == 'Female']   #extract the female dataframe
p_hat2 = len(record.loc[(record['num_procedures'] >=2) & (record['gender'] == 'Female')])/len(group5)#get the percentage which procedures is greater than 2
lb2 = p_hat2 - 1.96 * np.sqrt(p_hat2 * (1 - p_hat2) / len(group5))   #get the lower bound 
rb2 = p_hat2 + 1.96 * np.sqrt(p_hat2 * (1 - p_hat2) / len(group5))  #get the upper bound
print(lb1, rb1,lb2,rb2) #print the result

'''
the 95% condidence interval for male and female are:
Male: [0.3551161035669802 0.36378730733515563]   
Female: [0.31516986803938 0.32298177340245665]
'''

## 4.  Among the patients in this data set, what percentage had more than
##     one recorded hospital visit?  (Each distinct record can be assumed 
##     to be for a distinct hospital visit.)

group6 = record['patient_nbr'].groupby(record['patient_nbr']).count()   #count the number of each patient 
result5 = len(group6[group6 > 1])*100/len(group6)   #get the percentage which has more than one record
print(result5)  #print the result
'''
the percentage is 23.452837048015883%
'''

## 5.  List the top-10 most common diagnoses, based on the codes listed in
##     the columns 'diag_1', 'diag_2', and 'diag_3'.


diag_1 = record['diag_1'].groupby(record['diag_1']).count().sort_values(ascending=False)    #get the diag_1 dataframe and count the number
diag_2 = record['diag_2'].groupby(record['diag_2']).count().sort_values(ascending=False)    #get the diag_2 dataframe and count the number
diag_3 = record['diag_3'].groupby(record['diag_3']).count().sort_values(ascending=False)    #get the diag_3 dataframe and count the number
diag_4 = diag_1+ diag_2 + diag_3    #add such three dataframes 
print(diag_4.sort_values(ascending=False)[0:10])    #sort and print the top 10 result
'''
428    18101.0
250    17861.0
276    13816.0
414    12895.0
401    12371.0
427    11757.0
599     6824.0
496     5990.0
403     5693.0
486     5455.0
dtype: float64
'''
## 6.  The 'age' in each record is given as a 10-year range of ages.  Assume
##     that the age for a person is the middle of the range.  (For instance,
##     those with 'age' [40,50) are assumed to be 45.)  Determine the average
##     age for each classification in 'insulin'.

group7 = record[['age','insulin']]  #extract the dataframe with age and insulin
group7['average']= ''    #create a new colume
temp1 = np.zeros(len(group7))   #create a new array to store the value
for i in range(len(group7)):    #set the for loop
    temp1[i] = int(re.findall("\d+",group7.loc[i,'age'])[0]) + 5    #calculate the average age and store it into the array
group7['average'] = temp1    #pass the value into dataframe
group8 = group7['average'].groupby(group7['insulin']).mean()    #get the mean value group by each insulin type
print(group8)   #print the result
'''
insulin
Down      63.300049
No        67.460165
Steady    65.571169
Up        63.673560
Name: average, dtype: float64
'''

## 7.  Among those whose weight range is given, assume that the actual
##     weight is at the midpoint of the given interval.  If the weight is
##     listed as '>200' then assume the actual weight is 200.  Determine the
##     average weight for those whose 'num_lab_procedures' exceeds 50,
##     then do the same for those that are fewer than 30.

group9 = record[record['weight'] != '?']    #extract the dataframe which contains the weigth
group9['weight2'] = ''    #set the new empty colum
temp2 = np.zeros(len(group9))    #create a new array
for i in range(len(group9)):    #set the for loop 
    if (group9.iloc[i]['weight'] == '>200'):    #if the weight exceeds 200, set it to 200
        temp2[i] = 200  #set the weight
    else:
        index1 = int(re.findall("\d+",group9.iloc[i]['weight'])[0]) #get the first number
        index2 = int(re.findall("\d+",group9.iloc[i]['weight'])[1]) #get the second number
        weight = (index1+index2)/2  #get the average weight
        temp2[i] = weight   #set the average weight
group9['weight2'] = temp2   #pass the value to the dataframe
result7 = group9[group9['num_lab_procedures'] > 50]['weight2'].mean()   #get the mean value
result8 = group9[group9['num_lab_procedures'] < 30]['weight2'].mean()   #get the mean value
print(result7,result8)  #print the result
'''
the average weight exceeds 50 is :
85.05018489170628

the average weight fewer than 30 is :
88.73546511627907
'''

## 8.  Three medications for type 2 diabetes are 'glipizide', 'glimepiride',
##     and 'glyburide'.  There are columns in the data for each of these.
##     Determine the number of records for which at least two of these
##     are listed as 'Steady'.

temp3 = np.zeros(len(record))   #create a empty array
record['juge'] = ''    #create a new colum
for i in range(len(record)):    #set the for loop
    num = 0     #set the index
    if record.loc[i,'glipizide'] == 'Steady':   #if the patient have one type
        num += 1    #add 1
    if record.loc[i,'glimepiride'] == 'Steady': #if the patient have one type
        num += 1    #add 1
    if record.loc[i,'glyburide'] == 'Steady':   #if the patient have one type
        num += 1    #add 1
    if num >= 2:    #if the patient has at least two types
        temp3[i] = 1    #set 1 to the array
    else:
        temp3[i] = 0    #set 0
print(temp3.sum())  #print the total number of patients
'''
the number of records for which at least two of these are listed as 'Steady' is:
284
'''

## 9.  What percentage of reasons for admission ('admission_source_id')
##     correspond to some form of transfer from another care source?

samp = [4,5,6,10,18,22,25,26]   #sample which contains all transfer id
temp4 = np.zeros(len(record))   #create a empty array
record['care'] = ''    #set the empty colume
for i in range(len(record)):    #ste the for loop
    if record.loc[i,'admission_source_id'] in samp: #if the patient comes frome the sample
        temp4[i] = 1    #set 1 in the array
print(temp4.sum()*100/len(record))  #calculate the percentage and print the result
'''
the percentage is 6.218186820745633%
'''
## 10. The column 'discharge_disposition_id' gives codes for discharges.
##     Determine which codes (and the corresponding outcomes from the ID
##     file) resulted in no readmissions ('NO' under 'readmitted').  Then
##     find the top-5 outcomes that resulted in readmissions, in terms of
##     the percentage of times readmission was required.

group10 = record[record['readmitted'] != 'NO']  #extract the dataframe which does not have no readmission
result13 = record['discharge_disposition_id'].groupby(record['discharge_disposition_id']).count()   #count the total number
result12 = group10['discharge_disposition_id'].groupby(group10['discharge_disposition_id']).count()*100/result13  #count the extracted dataframe's number and get the percentage
final = result12.sort_values(ascending=False)   #sort the percentage
print(final.index[-3:]) #the ids' result in no readmissions are those whose percentages are 'Nan', print them
print(final[0:5])   #print the top-5 result

'''
the code result in no readmissions are:
[11, 19, 20]
'''

'''
the percentage is :
discharge_disposition_id
15    73.015873%
12    66.666667%
10    66.666667%
28    61.151079%
16    54.545455%
Name: discharge_disposition_id, dtype: float64
'''




