# JobChaser

A video to see how the program runs: https://youtu.be/Nwx3cAbwe9U

## Contents

Background
Installation
Usage


## Background

A report shows that in Australia,  there are over 20,000 people per month seeking for a job, but jobs opening are posted in many different platforms, which makes it difficult to search. Therefore, we designed this product to integrate information efficiently, which can save time for both job seekers and recruiters. Job seekers can find desired job information with ease, receive some practical advice to find ideal jobs and get some recommendations about online courses to sharpen their competitiveness. Companies can post jobs here and find some insights to improve recruitement plan. 


## Installation

#### PyPI

$ pip install numpy
$ pip install pandas
$ pip install xlwt
$ pip install xlrd
$ pip install seaborn
$ python -m pip install matplotlib
$ pip install beautifulsoup4 
$ pip install -U selenium

#### conda

$ conda install numpy
$ conda install pandas
$ conda install xlwt
$ conda install xlrd
$ conda install seaborn
$ conda install matplotlib
$ conda install beautifulsoup4
$ conda install -c conda-forge selenium

### Selenium Installation

You should do this first:
 $ conda install selenium
You need to pay attention to the Webdriver: https://selenium-python.readthedocs.io/install


We tested ChromeDriver and FirefoxDriver on MAC and Windows, and we recommend you:
For Mac: Chrome is better, but sometimes it may need to add a driver path to the code.
For Windows: Both can be run without adding a path to the code.

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/1.png)

The function 'openBrowser()' is defined in jobInfo\JobSearch.py and jobInfo\Oneshift.py 


#### For mac(If you use ChromeDriver)

chromedriver download: http://npm.taobao.org/mirrors/chromedriver/ (please check your chromedriver version)

Download the corresponding zip package of your own system, unzip the package.
Then import into the bin folder:
Open Finder, use Command+Shift+G,
Type /usr/local/bin in the directory 
Drag the unzipped Chromedrive.exe file into it

After this, you can run our code for the ChromeDriver in jobInfo/JobSearch.py and jobInfo/Oneshift.py as below
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

Because the MAC path is pretty much the same, we've already written the code ahead of time, if the main program still cannot open a browser, please modify this line "driver = webdriver.Chrome(executable_path=' ') " using a correct path.


You need to pay atttention to the environment vairables.

Configure environment variables：
$ vim ~/.bash_profile
$ export PATH=$PATH:/usr/local/bin/ChromeDriver
$ ：wq!
$ source ~/.bash_profile 
If you have any question, please check this website.

#### For mac(If you use FirefoxDriver)

Driver download: https://github.com/mozilla/geckodriver/releases (please check your Firefoxdriver version)
Download the corresponding zip package of your own system, unzip the package.
Then import into the bin folder:
Open Finder, use Command+Shift+G,
Type /usr/local/bin in the directory 
Drag the unzipped file into it

After this, you can run our code for the FirefoxDriver in jobInfo/JobSearch.py and jobInfo/Oneshift.py as below.

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

if the main program still cannot open a browser, please modify this line "driver = webdriver.Firefox(executable_path=' ') " using a correct path.

You need to pay atttention to the environment vairables.

Configure environment variables：
$ sudo vi ~/.bash_profile
$ export PATH=$PATH:/usr/local/bin/geckodriver
$ ：wq!
$ source ~/.bash_profile


#### For Windows(If you use ChromeDriver)

chromedriver download: http://npm.taobao.org/mirrors/chromedriver/ (please check your chromedriver version)

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/2.png)

For example: If the Chrome version is 86.0.4240.75,
You can download this version: http://npm.taobao.org/mirrors/chromedriver/86.0.4240.22/
Place chromedriver.exe in the Scripts directory under the anaconda installation path, for example: 

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/3.png)

#### For Windows(If you use FirefoxDriver)

Driver download: https://github.com/mozilla/geckodriver/releases (please check your Firefoxdriver version)
Similarly Download the corresponding driver according to your own operating system. If you use it, you need to add the path of the driver and the path of the Firefox browser to the environment variables


## Usage

### Setting environment variables

If a wavy line appears when you import our project, please follow this step as below:

SET both package and demo3 as source root,and then press Ctrl+s to save.
Then in Settings, select Add Source Roots to PYTHONPATH, Add sources root to PYTHONPATH,Then apply.

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/4.png)

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/5.png)


### Project Structure

To run this project, you only need to run the group_1_jobchaser_main.py program. All the other py program will be imported and called in group_1_jobchaser_main.py .

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/6.png)


### Detailed instruction for each py program

#### main.py

This py program is a user interface. Once you run it, it shows a main menu as follows:

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/7.png)

Users are asked to input a character and make a choice. Input "q" will exit the program. Input "1"  and "2" will lead you to the employer interface and job chaser interface respectively.

Here is the employer interface. 

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/8.png)

Input "1"  to post a job.

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/9.png)

Input details respectively and press "enter" to submit. Then it will lead you back to the main menu.

Input "2" to get labor market insights.

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/10.png)

Here is the job chaser interface.

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/11.png)

In the job chaser interface, input 1 to find a job, and input the job that you want to know about( here I input "engineer" as an example).

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/12.png)

Then it returns a list of 10 search results.

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/13.png)

To see more job information, Input "Y". If input "N", the program will stop showing search results and recommend some relevant courses for you to improve yourself. If the matched courses are not sufficient, we will also recommend some useful general courses to help you improve skills in other respects, such as leadership, programming and psychology. These courses will also benefit you a lot!

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/14.png)

Then input "q" to return to the main menu.

In the job chaser interface, input 2 to get some insights.

![image](https://github.com/github-jpk/JobChaser/blob/main/images/readme_images/15.png)

The same as above, you can then Input "q" to return to the main menu and exit the program.

#### Adzuna.py

This py program is to show the jobs information from Adzuna,which can be recommended to users. We used beautifulsoup4 to crawl 2000 job information.  We converted those information to dataframe and it  will be imported in updateDatabase.py. The py file will take a lot of time (about 5-7 minutes). :D
We use two techniques to crawl job information: Beautifulsoup4 and Selenium. Beautifulsoup4 will take a long time to crawl job information. Therefore,we integrate them into the Jobdatabase.csv file that will be called later when the job query is done.  In the meantime, we've used Selenium to mimic the keyboard and mouse in typing directly what we want to crawl on a web page. When querying for a job in the main function, you will first use Selenium to crawl the information for the job, and then search for the job from the Jobdatabase.csv that has been crawled.

#### Oneshift.py

This py program is designed to scrape job information from Oneshift, an Australian online job network. We use Selenium to run a real-time web scraper to extract jobs from oneshift. Users can pass a jobTitle to the function scrape_from_Oneshift, then the program will automatically search  jobTitle in Oneshift, scrape the search results, and return a dataframe that lists all the jobs finded.
This py program will be imported by: job_matching.py and  group_1_jobchaser_main.py.

#### Monster.py

This py program is to show the latest two days' job information in Australia from Monster. We mainly use regular expressions to match job information from the HTML file of the webiste, which is converted through beautifulsoup4. We create a DataFrame variable monster to save these information. This program will be imported by updateDatabase.py, which calls the monster variable in Monster.py to obtain the job information.

#### JobSearch.py

This py program is designed to scrape job information from JobSearch. We use Selenium to run a real-time web scraper to extract jobs from oneshift. Users can pass a jobTitle to the function scrape_from_JobSearch, then the program will automatically search  jobTitle in Oneshift, scrape the search results, and return a dataframe that lists all the jobs finded. This py program will be imported by: preprocessing.py and userinterface.py

#### seek.py

This py program is designed to scrape job information from Seek. The program includes getData, askURL and main functions. It can either run a real-time web scraper according to the job type input by the user or directly scrape all the job information and produce a local database. This program will be imported by updateDatabase.py and job_matching.py.

#### Course.py

This py program is to show the courses information from onlinestudies, we crawled those information and then converted them into dataframe.And the duplicate courses will be dropped.The job seekers can get suggestions on taking useful online courses.This program will be imported by course_matching.py.

#### updateDatabase.py

We integrate three dataframes together from Adzuna.py,Monster.py and Seek.py. The duplicate job will be dropped. Finally, this will produce a csv file（jobDatabase.csv). This program will be imported by group_1_jobchaser_main.py.

#### course_matching.py

We define matchCourse function to match the keyword with course titles through regular expressions. In this function, Course.csv will be read. In case no course is matched from our course resource, we also provide some general courses as complements. Duplicate courses will be dropped, and finally the function will return a DataFrame of recommended courses. This program will be imported by group_1_jobchaser_main.py.

#### CareerInsights.py

This py program is designed to generate some insights for companies and job seekers, based on data from Australian Bureau of Statistics. This program reads two files: preprocessing.csv and CareerInsights.csv. 

#### job_matching.py

We integrate job information together from Oneshift.py,seek.py and Jobsearch.py into jobDatabase.csv. Because it can choose different kinds of job at first. This program will be imported by group_1_jobchaser_main.py.
