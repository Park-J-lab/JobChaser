#!/usr/bin/env python
# coding: utf-8


"""
    Title:JobSearch.py
    Author: Panke Jing, pjing@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program is designed to scrape job information from jobsearch.gov.au .
    JobSearch is a free recruitment database funded by the government. As a platform provided by the government, 
    in addition to looking for a job, there are many authoritative first-hand information and handbooks for users' reference, 
    such as guidebooks for Australia, information on training and job search services, and some useful data on jobs and industries.
    This py program will be imported by: job_matching.py
"""

import pandas as pd
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


def scrape_from_JobSearch(jobTitle) :
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
    
    # Enter the website
    driver.get("https://jobsearch.gov.au/job/search")

    # search for job information using the keyword input by the user
    driver.find_element_by_id("Keyword").send_keys(jobTitle)

    # then click "Search" button
    driver.find_element_by_xpath('/html/body/main/div[3]/section/form/section/div/div/div/fieldset/div[5]/button').click()
    sleep(10)

    # get the html document of the page
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    driver.close()

    # find the paragraph that is related to employment information through BeautifulSoup
    bs = BeautifulSoup(html, "html.parser")
    results = bs.find_all(name="li", attrs={"class" :"result"})
    
    return results


def getJobInfo(results) :

    """
        # analyze the html of the web page that contains the job information #
        :param results: the html document preprocessed by BeautifulSoup
    """
    
    # store different fields of each piece of job information
    info_link = []
    job_title = []
    location = []
    salary = []
    job_decription = []
    company_name = []
    year = []
    month = []
    day = []
    
    # extract and store proper information from the web page
    for i in range(len(results)):

        cur_result = str(results[i])

        # Information link
        info_begin = cur_result.find('<a href=')
        info_end = cur_result.find('>',info_begin)
        cur_info_link = "https://jobsearch.gov.au/" + cur_result[info_begin + 9 : info_end - 1]
        info_link.append(cur_info_link)

        # Job title
        job_begin = info_end + 1
        job_end = cur_result.find('<',job_begin)
        cur_job_title = cur_result[job_begin : job_end].replace('&amp;','&')
        job_title.append(cur_job_title)

        # Location
        location_begin = cur_result.find('upCaseSuburb') + 14
        location_end = cur_result.find('<',location_begin)
        cur_location = cur_result[location_begin : location_end].upper()
        location.append(cur_location)

        # Job Description
        job_description_begin = cur_result.find('<p>', location_end) + 3
        job_description_end = cur_result.find('...') + 3
        cur_job_description = cur_result[job_description_begin : job_description_end].strip().replace('&amp;','&')
        job_decription.append(cur_job_description)

        # Company name
        company_begin = cur_result.find('Company:',location_end)
        company_end = cur_result.find('Location',company_begin)
        cur_company_name = ''
        if company_begin * company_end <= 1:
            cur_company_name = '*Follow the link to learn more.'
        else:
            cur_company_name = cur_result[company_begin + 8 : company_end].strip().replace('&amp;','&').upper()
        company_name.append(cur_company_name)

        # Post date
        date_begin = cur_result.find('Date added:')
        date_begin_1 = cur_result.find(',', date_begin)
        date_end = cur_result.find('<', date_begin_1)
        cur_date = cur_result[date_begin_1 + 1 : date_end].strip()
        cur_date = cur_date.split(' ')
        day.append(cur_date[0])
        month.append(getMonthNum(cur_date[1]))
        year.append(cur_date[2])

    # some websites display salary information, but this website does not provide this
    salary = ['Not provided'] * len(job_title)
    
    # convert the extracted information into a DataFrame
    dict_form = dict(zip(['JobTitle', 'Company', 'Location', 'Year', 'Month', 'Day', 'JobDescription', 'Salary', 'Link'],
                         [job_title, company_name, location, year, month, day, job_decription, salary, info_link]))
    df_form = pd.DataFrame(dict_form)
    df_form.index = range(1, df_form.shape[0] + 1)
    
    return df_form


def getMonthNum(x):
    return{
        'January':1,
        'February ':2,
        'March':3,
        'April':4,
        'May':5,
        'June':6,
        'July':7,
        'August':8,
        'September':9,
        'October':10,
        'November':11,
        'December ':12,
    }.get(x,10)


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

