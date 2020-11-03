#!/usr/bin/env python
# coding: utf-8


"""
    Title:Oneshift.py
    Author: Zhengqian Luo, zhengqil@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program is designed to scrape job information from Oneshift. 
    Oneshift is an Australian online job network which matches employees with employers. 
    This can be anything from one-off shifts, casual work or permanent employment, 
    but most of the jobs here are part-time jobs. Both job seekers and businesses can sign-up for free.
    This py program will be imported by: job_matching.py
"""



import pandas as pd
import datetime
from urllib.request import urlopen 
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup



def openBrowser():
    """
        # open a browser, Chrome, Firefox, Edge or IE is needed to be installed #
    """
    try:
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        return driver
    except Exception as e:
        try:
            driver = webdriver.Chrome()
            return driver
        except Exception as e:
            print("\n\tFail to open Chrome on this PC, trying to open Firefox...")
            try:
                driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
                print("\tSuccessfully open Firefox, now continue to execute...")
                return driver
            except Exception as e:
                try:
                    driver = webdriver.Firefox()
                    print("\tSuccessfully open Firefox, now continue to execute...")
                    return driver
                except Exception as e:
                    print("\tFail to open Firefox either, trying to open Edge...")
                    try:
                        driver = webdriver.Edge()
                        print("\tSuccessfully open Edge, now continue to execute...")
                        return driver
                    except Exception as e:
                        print("\tFail to open Edge either, trying to open IE...")
                        try:
                            driver = webdriver.Ie()
                            print("\tSuccessfully open IE, now continue to execute...")
                            return driver
                        except Exception as e:
                            print("\tFail to open IE either, break now! Please refer to 'Installation' in Readme document to find how to solve this.\n")
                            return False



def scrape_from_Oneshift(jobTitle) :
    results = getHTML(jobTitle)
    
    if isinstance(results, bool):
        return False
    else:
        return getJobInfo(results)


def getHTML(jobTitle) :
    """
        # search for employment information according to the keyword input by user, return the html of the web page#
        :param jobTitle: title of the job that user want to search for, like 'data scientist', 'accountant', etc.
    """
    
    # supported browser: Safari, Chrome, Firefox, Edge, IE
    driver = openBrowser()
    
    if isinstance(driver, bool):
        print("****** There was an exception when trying to open a browser through webdriver. ******")
        return False

    driver.get("https://au.oneshiftjobs.com/")

    driver.find_element_by_class_name("form-control").send_keys(jobTitle)
    driver.find_element_by_tag_name("button").click()
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    
    driver.close()
    
    bsyc = BeautifulSoup(html, "html.parser")
    results = bsyc.select('div.searchResultItem a')
    return(results)
    



def getJobInfo(results) :

    """
        # analyze the html of the web page that contains the job information #
        :param results: the html document preprocessed by BeautifulSoup
    """
    jobtitle = []
    location = []
    createtime = []
    link = []

    for i in range(0,len(results),2):
        jobtitle.append(results[i].contents[1].contents[1].contents[1].find_all(name = 'h2')[0])
        location.append(results[i].contents[1].contents[1].contents[1].find_all(name = 'div',class_ = 'locationAt'))
        createtime.append( results[i].contents[1].contents[1].contents[1].find_all(name = 'div',class_ = 'createdAt'))
        link.append(results[i].attrs)

    jobtitle = [str(x)[4:-5] for x in jobtitle]
    location = [str(x)[33:-16] for x in location]
    createtime = [ str(x)[24:-7] for x in createtime]
    link = ['https://au.oneshiftjobs.com'+x['href'] for x in link]
    today=datetime.date.today()
    createtime = [today + datetime.timedelta(days=-transform_date(time)) for time in createtime]
    year = [i.year for i in createtime]
    month = [i.month for i in createtime]
    day = [i.day for i in createtime]

    df_form = pd.DataFrame(dict(zip(['JobTitle', 'Company', 'Location', 'Year', 'Month', 'Day', 'JobDescription', 'Salary', 'Link'],
                            [jobtitle,["Not Provided"]*len(jobtitle),location,year,month,day,["Check in link"]*len(jobtitle),["Not Provided"]*len(jobtitle),link])))

    return df_form




def transform_date(time):

    if "hours" in time:
        return 0
    else:
        return int(time.split(" ")[0])
    

