import requests
from bs4 import BeautifulSoup

webcontent = requests.get('http://www.mtsu.edu')

webcontent_soup = BeautifulSoup(webcontent.text, 'html.parser')

webcontent_ptags = webcontent_soup.find_all('p')

for link in webcontent_ptags:
    print(link)
    print()
