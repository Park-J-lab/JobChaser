#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- codeing = utf-8 -*-
'''
Title: updateDatabase.py
Author:
Guojiang Zhao, guojianz@andrew.cmu.edu
Kehan Wang, kehanw@andrew.cmu.edu
Zhengqian Luo, zhengqil@andrew.cmu.edu
Group Number:  1

Introduction: This py program is to perform three tasks: 
a) create local database by concating data from various websites
(removed) b) match online courses with jobs to make recommendations to users.
(removed) c) generate insights for companies and job seekers
(removed) This py program will be imported by : userinterface.py
And the modules we use are Adzuna、JobSearch、Monster、seek、Oneshift
'''

#import local data source
import Adzuna, Monster, seek


#create local databse by concating data from Adzuna, Monster, Seek

Adzuna = Adzuna.df_form2
Monster = Monster.monster
Seek = seek.Seekresult

LocalData = Adzuna.append(Monster)
LocalData = LocalData.append(Seek)
LocalData.drop_duplicates()
LocalData.drop_duplicates(['Link'])
LocalData.sort_values(by=["Month",'Day'],axis=0,ascending=False,inplace=True)
LocalData.index=range(len(LocalData))
LocalData.to_csv('jobInfo/jobDatabase.csv',encoding="utf_8_sig")


