#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Title:Seek.py
    Author: Kun Liu, kunliu@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program is designed to scrape job information from Seek.com.
    Seek.com is a website focus on Australia's jobs, employment, career and recruitment.  
    Users can input a certain jobtype and corresponding jobs will be provided.
    The program includes getData, askURL and main functions.
    We use getData function to convert the source to an HTML-aware BeautifulSoup object, and obtain raw       data from it.
    The core codes are about regular expressions. The function uses different methods of re, such as           findall and sub.
    This py program need to import BeautifulSoup,re,pandas,urllib.request,datetime,dateutil.relativedelta
    This py program will be imported by : updateDatabase.py, job_matching.py
'''

from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request
import datetime
from dateutil.relativedelta import relativedelta

findLink = re.compile(r'<a.*href="(.*)" target="_self">') 
findSalary = re.compile(r'Salary: (.*)" class="_3FrNV7v _3PZrylH E6m4BZb') 
findTime = re.compile(r'<span.*"jobListingDate">(.*)</span>') 
findCompany = re.compile(r'aria-label="Jobs at (.*)" class=.*jobCompany"')
findLocation = re.compile('"Limit results to (.*)" class=.*jobLocation"') 
findTitle = re.compile(r'aria-label="(.*)" class=.*data-automation.*data-job-id') 
Seekresult = pd.DataFrame(columns=["JobTitle","Company","Location","Year","Month","Day", "JobDescription","Salary","Link"])


def scrape_from_seek(jobtype=" "):   # print in a jobtype
    baseurl = "https://www.seek.com.au/jobs/in-All-Australia"
    return getData(baseurl,Seekresult,jobtype)
    


def getData(baseurl,Seekresult,jobtype=" "): #user can imput a jobtype, convert the source to a HTML-aware BeautifulSoup object
    if jobtype!=" ":
        jobtype = jobtype.replace(" ", "-")
        baseurl = baseurl[0:24]+jobtype+"-"+baseurl[24:] #search as the user type in a certain jobtype
    lst = []
    for i in range(1,5): # set page range of information we want to scrap
        if i>1:
            url=baseurl+'?page='+str(i)
        else:
            url=baseurl
        html = askURL(url)  
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all(name='article', attrs={"data-automation":"premiumJob","data-automation":"normalJob"}):
            item = str(item)      
            Title = re.findall(findTitle, item)
            lst.append(Title[0])
            try:
                Company = re.findall(findCompany, item)[0]
            except Exception:
                Company = 'Private Adviser'
            lst.append(Company)
            Location = re.findall(findLocation, item) 
            lst.append(Location[0])
            Time = re.findall(findTime, item)[0][0:7]
            if Time[-1] =='<':
                Time = Time[:-1]
            if Time.find('m') == 1:
                n = int(Time[-7:-5])
                date = datetime.date.today() - relativedelta(months=-n)
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                day = datetime.datetime.now().day
                
            elif Time.find('d') == 1:
                n = int(Time[-7:-5])
                date = datetime.date.today() + datetime.timedelta(-n)
                year = date.year
                month = date.month
                day = date.day
            else: 
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                day = datetime.datetime.now().day        
            lst.append(year)
            lst.append(month)
            lst.append(day)
            jobdescription = "Check in link"
            lst.append(jobdescription)
            try:
                Salary = re.findall(findSalary, item)[0]
            except Exception:
                Salary = 'Not provided'
            lst.append(Salary)
            Link = re.findall(findLink, item)
            Link = "https://www.seek.com.au"+Link[0]
            lst.append(Link)
    length = int(len(lst)/9)
    for i in range(length):
        Seekresult.loc[i] = [lst[9 * i + 0], lst[9 * i + 1], lst[9 * i + 2], lst[9 * i + 3],
                            lst[9 * i + 4], lst[9 * i + 5], lst[9 * i + 6],
                            lst[9 * i + 7], lst[9 * i + 8]]  
    return Seekresult

      

def askURL(url): #obtain html content from website
    head={ 
       "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4263.3 Safari/537.36"
}  
    request = urllib.request.Request(url,headers= head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html= response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html



