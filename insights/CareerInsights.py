#!/usr/bin/env python
# coding: utf-8

'''
    Title:CareerInsights.py
    Author: Zhengqian Luo, zhengqil@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program is designed to generate some insights for companies and job seekers, based on data from Australian Bureau of Statistics
    This py program will be imported by: group_1_jobchaser_main.py
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


def show_insight(users):
    if users == "companies":
        jobs_wages_trends()
        Wage_change_by_states(3)
    # more functions to be added
    if users == "job seekers":
        Wage_change_by_states(1)
        Wage_change_by_industry()
        top_locations_recruting()
        top_companies_recruting()


def jobs_wages_trends():
    indexTrends = pd.read_excel("insights/CareerInsights.xlsx", sheet_name="Index trends",header=1)
    indexTrends['Week ending'] = [i[:-5] for i in indexTrends['Week ending']]
    indexTrends_line = indexTrends.plot(x="Week ending",title="Weekly Payroll Jobs and Wages in Australia in 2020", xticks = list(range(26)), rot=45, figsize=(10,5) )
    print("\t--------------------------------------------------------------------------------------------")
    print("\t1. The number of payroll jobs dropped significantly since March, probably due to the impact")
    print("\tof COVID-19 and hit bottom in the mid of April.Now the economy is recovering soon.")
    print("\n\t2. Total wage index also dropped greatly since the outbreak of COVID-19.It hit bottom on 23")
    print("\tMay and reached a peak in 4 July. Although it fell back then, its performance now is still ")
    print("\tmuch better than the first half of 2020.")
    print("\n\tWe can be more optimistic as Australia returning to its normal state step by step.")
    plt.show()

def Wage_change_by_states(k):
    percentageByStates = pd.read_excel("insights/CareerInsights.xlsx", sheet_name="Percentage change by states",header=1)
    percentageByStates = percentageByStates.drop(columns=percentageByStates.columns[1:-1])
    percentageByStates.columns = ['States', 'Percentage Change']
    percentageByStates_barh = percentageByStates.plot(x ="States" ,kind='barh', title= "Wage Percentage change between 14 Mar. and 19 Sept. by states in 2020",figsize=(8,5) )
    print("\t--------------------------------------------------------------------------------------------")
    print("\t" + str(k) + ". The overall wage in Australia in September has decreased by 3% compared with March, but")
    print("\t South Australia sees a delightful increase, though very slightly.")
    print("\n\tWe advise job seekers to go to SA for better paid jobs.")

    plt.show()


def Wage_change_by_industry():
    wageChangeByIndustry = pd.read_excel('insights/CareerInsights.xlsx', sheet_name="Wage change by industry")
    wageChangeByIndustry.plot(x="Industry name", xticks=list(range(19)), kind='barh', xlim=(0, 3),
                              title="Wage change by industry", figsize=(8, 8))
    print("\t--------------------------------------------------------------------------------------------")
    print("\t2. Wage has increased by 2% on a year-over-year basis. Most industry experience a positive")
    print("\tgrowth on a quarter-over-quarter basis.")
    print("\n\tWe recommend job seekers to go to the following promising industries: electricity, gas and")
    print("\twaste service, mining,education and training")

    plt.show()

#show Top 20 locations that post most jobs in the last two weeks
def top_locations_recruting():
    database = pd.read_csv('jobInfo/jobDatabase.csv')
    d_14 = datetime.date.today()-datetime.timedelta(days=14)
    selected = database[database['Year']>= d_14.year ]
    selected = selected[selected['Month']>=d_14.month]
    selected = selected[selected['Day']>= d_14.day]
    locations = selected.groupby(['Location']).count().sort_values(by=['JobTitle'],ascending = False).head(20)
    locations = locations.iloc[:,1:2]
    locations.columns = ['# of job posted in the past two weeks']
    print("\t--------------------------------------------------------------------------------------------")
    print("\t3. Locations below are in urgent need of talents. We advise you to have a try.")
    locations.plot(kind='barh')
    plt.show()


#show Top 20 companies that post most jobs in the last two weeks
def top_companies_recruting():
    database = pd.read_csv('jobInfo/jobDatabase.csv')
    d_14 = datetime.date.today()-datetime.timedelta(days=14)
    selected = database[database['Year']>= d_14.year ]
    selected = selected[selected['Month']>=d_14.month]
    selected = selected[selected['Day']>= d_14.day]
    companies = selected.groupby(['Company']).count().sort_values(by=['JobTitle'],ascending = False).head(20)
    companies = companies.iloc[:,1:2]
    companies.columns = ['# of job posted in the past two weeks']
    print("\t--------------------------------------------------------------------------------------------")
    print("\t4. Companies below are in urgent need of talents. We advise you to have a try.")
    companies.plot(kind='barh')
    plt.show()