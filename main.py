
'''
    Title: group_1_jobchaser_main.py
    Author: Kun Liu, kunliu@andrew.cmu.edu
            Panke Jing, pjing@andrew.cmu.edu
    Group Number:  1
    Introduction: This py program is our main program, it realize the function for both companies and will scrape data from           seek.com, Oneshift.com and JobSearch.com imitating user is inputing a certain job type and also will match related jobs with       the given job type from the local database.
    This py program need to import seek,Oneshift,JobSearch,pandas and re
    This py program will be imported by : group_1_jobchaser_main.py
    
'''
#CareerInsights.py is providing market insights
#course_matching.py recommends related course as you input a jobtype
#job_matching.py search related job vacancies from the websits and return job info
from insights import CareerInsights as cis
from courseInfo import course_matching as cm
from jobInfo import job_matching as jm
from IPython.display import display
import datetime
import pandas as pd
import re


answer = ''
pd.set_option('display.max_columns', None)  #ensure all columns show

while answer.lower() != 'q':

    print("\n--------------------------------------------------------------------------------------------")
    print("Hello, welcome to JobChaser!\n")
    print("Main Menu:")
    print("1)  I'm an employer.")
    print("2)  I'm a job chaser.")
    print("\nQ)  Quit from this program.")
    print("\nPlease select the function you want to by entering the option [1,2,Q].")

    answer = input("Your choice: ")
    answer = answer.strip()

    if answer == '1':

        companyanswer = ''

        print("\n\t--------------------------------------------------------------------------------------------")
        print("\tEmployees are your most important asset!")
        print("\tTrust JobChaser to help you find the right person!")
        print("\n\tYou want to:")
        print("\t1)  Post a job.")
        print("\t2)  Get labor market insigts.")
        print("\n\tQ)  Return to main menu.\n")

        companyanswer = input('\tYour choice: ')
        companyanswer = companyanswer.strip()

        if companyanswer == '1':

            print("\n\t\tPlease input the details below.\n")

            jobtitle = input('\t\tJob Title: ')
            jobtitle = jobtitle.strip()

            company = input('\t\tCompany: ')
            company = company.strip()

            location = input('\t\tLocation: ')
            location = location.strip()

            jobdescription = input("\t\tJob Description (If you would not like to type this information, just enter 'n': ")
            jobdescription = jobdescription.strip()
            if jobdescription.lower() == 'n':
                jobdescription = 'Check in link'

            salary = input("\t\tSalary (If salary is not specified, just enter 'n'): ")
            salary = salary.strip()
            if salary.lower() == 'n':
                salary = 'Not provided'

            link = input('\t\tPlease provide a link to the application page: ')
            link = link.strip()

            date = str(datetime.date.today()).split('-')
            year = date[0]
            month = date[1]
            day = date[2]

            headers = ['JobTitle', 'Company', 'Location', 'Year', 'Month', 'Day', 'JobDescription', 'Salary', 'Link']
            jobAd = [jobtitle, company, location, year, month, day, jobdescription, salary, link]

            df_new = pd.DataFrame([jobAd], columns=headers)
            df0 = pd.read_csv('jobInfo/jobDatabase.csv', index_col=0)

            df0 = pd.concat([df0, df_new], ignore_index=True)
            df0.to_csv('jobInfo/jobDatabase.csv')

            print('\n\tSuccessfully submitted!')

        elif companyanswer == '2':
            # be aware the plot may appear BEHIND other windows
            cis.show_insight(users="companies")

        elif companyanswer.lower() == 'q':
            pass  # go to main menu

        else:
            print('\n\tYour choice is not valid:', companyanswer)

        print("\t--------------------------------------------------------------------------------------------")
        print("\n\tNow return to main menu...")
    elif answer == '2':

        jobchaseranswer = ''
        print("\n\t--------------------------------------------------------------------------------------------")
        print("\tHi Friend!")
        print("\tWe are here you help you navigate the road ahead!")
        print("\n\tYou want to:")
        print("\t1)  Find a job.")
        print("\t2)  Get market insigts.")
        print("\n\tQ)  Return to main menu.\n")

        jobchaseranswer = input('\tYour choice: ')

        if jobchaseranswer.strip() == '1':
            jobtype = input("\n\tPlease input the position you are seeking: ")
            jobtype = jobtype.strip()

            print('\n\tLoading...\n')


            try:
                jobSearchresult = jm.job_match(jobtype)
            except Exception:
                db_data = pd.read_csv('jobInfo/jobDatabase.csv', index_col=0)
                jobSearchresult = db_data[db_data['JobTitle'].str.contains(jobtype,flags=re.IGNORECASE,regex=False)]
                jobSearchresult.sort_values(by=["Month",'Day'],axis=0,ascending=False,inplace=True)
                jobSearchresult = jobSearchresult.reset_index()

            i = 0
            nextpage = 'y'
            while nextpage.lower() == 'y' and (i*10+9) < len(jobSearchresult):
                print('\n')
                display(jobSearchresult[i*10:i*10+10])
                nextpage = input('\n\tDo you wanna see more employment information? (y/n): ')
                nextpage = nextpage.strip()
                i = i+1
                
            print("\n\t--------------------------------------------------------------------------------------------")
            print("\t\t And we also recommend some related skill-improving course for you! ")
            display(cm.matchCourse(jobtype))

        elif jobchaseranswer == '2':

            # be aware the plot may appear BEHIND other windows
            cis.show_insight(users="job seekers")

        elif jobchaseranswer.lower() == 'q':

            pass  # go to main menu

        else:
            print('\n\tYour choice is not valid:', jobchaseranswer)

        print("\t--------------------------------------------------------------------------------------------")
        print("\n\tNow return to main menu...")

    elif answer.lower() == 'q':

        pass  # the loop will terminate
        print("\nWe are looking forward to your coming next time. ^_^")
        print("--------------------------------------------------------------------------------------------")

    else:

        print('\nYour choice is not valid:', answer)