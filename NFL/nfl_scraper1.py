#2015-16 season scraper 

from lxml import html
import requests
from bs4 import BeautifulSoup

#FanDuel salaries

#QB's
qb_page = requests.get('http://www.fantasypros.com/nfl/fanduel-cheatsheet.php')
tree1 = qb_page.text

soup = BeautifulSoup(tree1, 'html.parser')

fd_qb_name = soup.find("div", {"class": "mobile-table"}).a.contents

print "Names: "
for line in fd_qb_name:
    print line
