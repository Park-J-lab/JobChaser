#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""   
    Title:job_matching.py
    Author: Kun Liu, kunliu@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program will scrape data from seek.com, Oneshift.com and JobSearch.com imitating user is inputing a         certain job type and also will match related jobs with the given job type from the local database.
    This py program need to import seek,Oneshift,JobSearch,pandas and re
    This py program will be imported by : group_1_jobchaser_main.py
    
"""
    
    
from jobInfo import seek,Oneshift,JobSearch
import pandas as pd 
import re


def job_match(jobtype):

    seekresult = seek.scrape_from_seek(jobtype)
    oneshiftresult = Oneshift.scrape_from_Oneshift(jobtype)
    jobSearchresult = JobSearch.scrape_from_JobSearch(jobtype)

    db_data = pd.read_csv('jobInfo/jobDatabase.csv', index_col=0)  
    db_data = db_data[db_data['JobTitle'].str.contains(jobtype,flags=re.IGNORECASE,regex=False)]

    jobdata = seekresult.append(db_data)
    if isinstance(oneshiftresult, pd.core.frame.DataFrame):
        jobdata = seekresult.append(oneshiftresult)
    if isinstance(jobSearchresult, pd.core.frame.DataFrame):
        jobdata = seekresult.append(jobSearchresult)

    jobdata.sort_values(by=["Month",'Day'],axis=0,ascending=False,inplace=True)
    jobdata = jobdata.reset_index()

    return jobdata