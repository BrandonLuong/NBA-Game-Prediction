from bs4 import BeautifulSoup
from bs4 import Comment
import pandas
import requests
import time
from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import chromedriver_binary

url = 'https://www.nba.com/stats/teams/boxscores/?Season=2021-22&SeasonType=Regular%20Season'

driver = wd.Chrome()
driver.get(url)

# #load webpage
# r = requests.get(url).text
# soup = BeautifulSoup(r, 'lxml')

# select = Select(driver.find_element_by_xpath())

select = Select(driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select"))

driver.implicitly_wait(1)
#select "All" option
select.select_by_index(0)

source = driver.page_source
soup = BeautifulSoup(source, 'lxml')
# table = soup.find('div', class_="nba-stat-table__overflow")
table = soup.find('div', attrs={"class" : "nba-stat-table__overflow"})

# get table headers
headers = table.find_all('th')
headers_list = [h.text.strip() for h in headers]

#get table rows (stats)
table_rows = table.find_all('tr')[1:]
row_list = []
# game_stats = [[td for td in rows[i].findAll('td')] for i in range(len(rows))]

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td]
    row_list.append(row)
