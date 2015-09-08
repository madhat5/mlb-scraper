#2015-16 season scraper 

from lxml import html
import requests
from bs4 import BeautifulSoup

#game times pull
page1 = requests.get('https://rotogrinders.com/lineups/mlb?site=fanduel')
tree1 = page1.text

soup = BeautifulSoup(tree1, 'html.parser')

#print times
times = soup.find_all("time")
print "Game Times: "
for line in times:
    print line.text
