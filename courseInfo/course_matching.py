#!/usr/bin/env python
# coding: utf-8

'''
    Title: course_matching.py
    Author: Kehan Wang, kehanw@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program is designed to match courses with job types. It will read the Course.csv file to obtain course informaion.
    This py program will be imported by: group_1_jobchaser_main.py
'''


import re
import pandas as pd
import random



#this function is designed to convert special characters into raw string, like '+' in 'C++'
def raw(text):
    escape_dict = {'+':'\+', '.':'\.'}
    rawText = ''
    for char in text:
        try:
            rawText += escape_dict[char]
        except Exception:
            rawText += char
    return rawText

#this function can be called to match keyword with course titles
def matchCourse(jobtype):
    df = pd.read_csv('courseInfo/Course.csv', index_col=0) #obtain all the course information in terms of DataFrame from Course.csv
    result = pd.DataFrame(columns=['Title','CourseType', 'Source','Link','Content']) #construct an empty DataFrame
    rawString = raw(jobtype)
    keyword = rawString.split() #get separate keywords, such as "data" and "analyst" in "data analyst"

    #if there is no exact matching result, we provide some useful general courses
    generalCourse = pd.DataFrame(columns=['Title', 'CourseType', 'Source', 'Link', 'Content'])
    general = re.compile('leadership|Microsoft Excel|programming|psychology', re.IGNORECASE)

    #loop to match course titles with keywords
    k = 0 #represent the row index of result
    j = 0 #represent the row index of generalCourse
    for i in range(df.shape[0]):
        #compare keywords with course title
        for num in range(len(keyword)):
            findCourse = re.compile(keyword[num], re.IGNORECASE)
            if len(re.findall(findCourse, df.iloc[i, 0])) != 0:
                result.loc[k] = [df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4]]
                k += 1
                break #in case the same course is selected more than once if it contains more than one keyword
        if  len(re.findall(general,df.iloc[i,0])) != 0:
            generalCourse.loc[j] = [df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4]]
            j += 1

    # check whether the matched course are not sufficient and at least provide 5 courses
    if k < 5:
        # randomly select the remaining courses from the general courses
        list = random.sample(range(generalCourse.shape[0]),5-k)
        for i in range(5-k):
            result.loc[k+i] = generalCourse.loc[list[i]]

    # in case the same course is selected more than once
    for i in range(result.shape[0]-1):
        for n in range(i+1,result.shape[0]):
            if result.iloc[i,0] == result.iloc[n,0]:
                result = result.drop(i)
                break

    result.index = range(1, result.shape[0] + 1)
    return result
