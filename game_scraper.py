from bs4 import BeautifulSoup
from bs4 import Comment
import pandas
import requests
import time
from selenium import webdriver as wd
import chromedriver_binary

url = 'https://www.nba.com/stats/teams/boxscores/?Season=2021-22&SeasonType=Regular%20Season'

driver = wd.Chrome()
driver.get(url)

# #load webpage
r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')

driver.find_element_by_xpath()



# comments = soup.find_all(string=lambda text: isinstance(text, Comment))
# # stat_table = soup.find('div', class_='row row5 collapse stats-filters-top')
# for comment in comments:
#     print(comment)
#     comment.extract()
# print(soup.prettify)