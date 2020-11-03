# -*- codeing = utf-8 -*-
'''
Title: Adzuna
Author: Guojiang Zhao, guojianz@andrew.cmu.edu 
Group Number:  1
Introduction: This py program is to show the jobs information from Adzuna,which can be recommended to users.
This py program will be imported by : updateDatabase.py
And the modules I use are BeautifulSoup、re、urllib.request、 urllib.error、pandas
'''
from bs4 import BeautifulSoup  # Web page analysis, Access to data
import re  # Regular expression, Text matching '
import urllib.request, urllib.error  # Make the URL and get the webpage data
import pandas as pd
import datetime

def askURL(url):
    head={   #Simulates header information and sends a message to the server
       "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4263.3 Safari/537.36"
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


baseurl = 'https://www.adzuna.com.au/search?ac_where=0&loc=98480&p='
findtitle = re.compile(r'<strong>(.*)</strong>')
datalist1 = []
companyorloclist1 = []  # the list of company or locations
titlelist1 = []  # the list of title
locationlist1 = []  # the list of location
contentslist1 = []  # the list of content
linklist1 = [] #the list of link
for i in range(1, 201):
    url = baseurl + str(i)
    html = askURL(url)

    bs = BeautifulSoup(html, 'html.parser')
    for item in bs.find_all('div', class_="a"):
        item_str = str(item)
        title = re.findall(findtitle, item_str)[0]  # Get the title name
        title = re.sub('&amp', '&', title)  # Convert &amp to &

        title = re.sub('&;', '&', title)  # Convert &; to &
        titlelist1.append(title)
        contents1 = item.find('span', class_="at_tr").get_text().strip()  # Get the contents

        contentslist1.append(contents1)
        company1 = item.find('p', class_='as').get_text().strip()  # Get the company name
        companyorloclist1.append(company1)

        location1 = item.find('span', class_="loc").get_text().strip()  # Get the location
        locationlist1.append(location1)
        link = item.find('h2').a['href']
        linklist1.append(link)


Yearlist=[]
Monthlist = []
Daylist = []
Salarylist=[]

for i in range(len(titlelist1)):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    Yearlist.append(year)
    Monthlist.append(month)
    Daylist.append(day)
    Salarylist.append('Not provided')
    


dict_form2 = dict(zip(['JobTitle', 'Company','Location','Year','Month','Day', 'JobDescription','Salary','Link'],[titlelist1,companyorloclist1,locationlist1,Yearlist,Monthlist,Daylist,contentslist1,Salarylist,linklist1]))
df_form2 = pd.DataFrame(dict_form2)
df_form2.index = range(1, df_form2.shape[0] + 1)
df_form2.to_csv('adzuna.csv',encoding="utf_8_sig")