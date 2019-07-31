from bs4 import BeautifulSoup
import os


file = 'downloads.html'

soup = BeautifulSoup(open(file), 'html.parser')

league = soup.find('span',{'style':'padding:10px 0;'})
print(league.text)
