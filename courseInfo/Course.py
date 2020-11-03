#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- codeing = utf-8 -*-
'''
Title: Course
Author: Guojiang Zhao, guojianz@andrew.cmu.edu 
Group Number:  1
Introduction: This py program is to show the courses,which can  be recommended to users.
The function of this program is to generate Course.csv .
The modules I use include BeautifulSoup、re、urllib.request、 urllib.error、xlwt、requests、numpy、pandas
'''
from bs4 import BeautifulSoup  # Web page analysis, Access to data
import re  # Regular expression, Text matching '
import urllib.request, urllib.error  # Make the URL and get the webpage data
import pandas as pd 


def askURL(url):
    head={   #Simulates header information and sends a message to the server
       "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}  # User agent that tells the browser what level of file content is acceptable
    request = urllib.request.Request(url,headers= head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html= response.read().decode('utf-8')
#         print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html



import time
time.sleep(2)
coursetypelist1 = [] # the list of coursetype
titlelist1 = []  #the list of title
sourcelist1 = []#the list of Source of course
linklist1 = [] #the list of link
contentslist1 = [] #the list of content
#computer course   len:59 No0-58
baseurl1='https://www.onlinestudies.com/Courses/Computer-Science/?page='
for i in range(1, 5):
        url = baseurl1+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Computer Course')
            
#business course   len:135  No.59-193
baseurl2='https://www.academiccourses.com/Business-Studies/?page='
for i in range(1, 10):
        url = baseurl2+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Business Course')

#law len(30)   No.194-223
baseurl3 = 'https://www.academiccourses.com/Law/?page='
for i in range(1, 3):
        url = baseurl3+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Law Course')
#media  len(60)          No.224-283
baseurl4 = 'https://www.academiccourses.com/Media/?page='
for i in range(1, 5):
        url = baseurl4+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Media Course')
# #social  len:60  284-343

baseurl5 ='https://www.academiccourses.com/Social-Sciences/?page='
for i in range(1, 5):
        url = baseurl5+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Social Science Course')
            
#HealthCare
baseurl6 ='https://www.onlinestudies.com/Courses/Mental-Healthcare/?page='
for i in range(1, 3):
        url = baseurl6+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('HealthCare Course')   
            
#Management
baseurl7 ='https://www.onlinestudies.com/Courses/Leadership/?page='
for i in range(1, 3):
        url = baseurl7+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Management Course')   
            
            
            
#Economic
baseurl8 ='https://www.onlinestudies.com/Courses/Economic-Studies/?page='
for i in range(1, 5):
        url = baseurl8+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Economic Course')   
            

#Education
baseurl9 ='https://www.onlinestudies.com/Courses/Teaching/?page='
for i in range(1, 3):
        url = baseurl9+str(i)
        html = askURL(url)
     
        bs = BeautifulSoup(html,'html.parser')
        for i in bs.find_all(name='div',class_="program-listitem relative"):  
            title = i.find('div',class_="title").get_text().strip()
            titlelist1.append(title)
            school= i.find('div',class_="school").get_text().strip()
            sourcelist1.append(school)
            link = i.find('div',class_="title").a['href']
            linklist1.append(link)
            content=i.find('p',class_="desc").get_text().strip()
            content = re.sub('\r','',content)
            content = re.sub('\n','',content)
            content = re.sub('\+','',content)
            content = re.sub('\t','',content)
            contentslist1.append(content)
            coursetypelist1.append('Education Course')  
dict_form2 = dict(zip(['Title','CourseType', 'Source','Link','Content'],[titlelist1,coursetypelist1,sourcelist1,linklist1,contentslist1]))
df_form2 = pd.DataFrame(dict_form2)
df_form2.drop_duplicates(['Title'])
df_form2.index = range(1, df_form2.shape[0] + 1)
df_form2.to_csv('Course.csv',encoding="utf_8_sig")


# In[ ]:




