#!/usr/bin/env python
# coding: utf-8

'''
    Title:Monster.py
    Author: Kehan Wang, kehanw@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program is designed to scrape job information from Monster.
    Monster is a worldwide job-searching website. And we are focusing on the Australia region.
    The program includes getData, askURL, saveData and main functions.
    We use getData function to convert the source to an HTML-aware BeautifulSoup object, and obtain raw data from it.
    The core codes are about regular expressions. The function uses different methods of re, such as findall and sub.
    Then we use saveData function to save data and return a DataFrame to the main function.
    This py program will be imported by : updateDatabase.py
'''

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import datetime
import pandas as pd

length = 0
findCompany = re.compile(r'<span class="name">(.*)</span>')
findTime = re.compile(r'<time datetime="2017-05-26T12:00">(.*)</time>')
findLink = re.compile(r'<a.* href="(.*)" onclick=.*>')
findSalary = re.compile(r'<p>.*Salary:(.*)</p>')
monster = pd.DataFrame(columns=["JobTitle","Company","Location","Year","Month","Day", "JobDescription","Salary","Link"])

def main():
    baseurl = "https://www.monster.com/jobs/search?q=&sort=rv&vw=b&re=14&brd=1&cy=AU&stpage=1&page=10"
    datalist = getData(baseurl)
    saveData(monster,datalist)

#convert the source to a HTML-aware BeautifulSoup object
def getData(baseurl):
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    datalist = []

    #loop to get the information of each job
    for item in soup.find_all('div', class_="flex-row"):
        #obtain the title of jobs
        title = item.a.string
        title = re.sub('\r', '', title)
        title = re.sub('\n', '', title)
        datalist.append(title)

        #obtain the company names
        item_str = str(item)
        company = re.findall(findCompany, item_str)[0] #probabaly find many results, but we only need the first one
        datalist.append(company)

        #obtain the location of jobs
        location = item.find('div',class_="location").get_text().strip()
        datalist.append(location)

        #obtain the posted time of jobs
        #the website provides the nearest two days' job information
        time = re.findall(findTime, item_str)[0]
        if str(time)=="Posted today":
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
        elif str(time)=="1 day ago":
            yesterday = datetime.date.today() + datetime.timedelta(-1)
            year = yesterday.year
            month = yesterday.month
            day = yesterday.day
        datalist.append(year)
        datalist.append(month)
        datalist.append(day)

        #The details about jobs are provided in the link
        jobdescription = 'Check in link'
        datalist.append(jobdescription)

        #Not all the jobs provide information of salary
        try:
            salary = re.findall(findSalary, item_str)[0]
        except Exception:
            salary = 'Not provided'
        datalist.append(salary)

        #obtain links about job details
        link = re.findall(findLink, item_str)[0]
        datalist.append(link)

    # the length measures how many jobs we have scraped
    global length
    length = int(len(datalist)/9)
    return datalist

#obtain the html from the website
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#save and add data to the input DataFrame
def saveData(df,datalist): 
    for i in range(length):
        df.loc[i] = [datalist[9*i+0],datalist[9*i+1],datalist[9*i+2],datalist[9*i+3],datalist[9*i+4],
                     datalist[9*i+5],datalist[9*i+6],datalist[9*i+7],datalist[9*i+8]]

main()
if __name__ == '__main__':
    print("Scraping data is ending.")
