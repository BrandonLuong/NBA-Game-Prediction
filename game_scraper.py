from bs4 import BeautifulSoup
import pandas
import requests

url = 'https://www.nba.com/stats/lineups/traditional/?Season=2021-22&SeasonType=Regular%20Season'

#load webpage
r = requests.get(url)
print(r)