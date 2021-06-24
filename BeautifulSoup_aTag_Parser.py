import requests
from bs4 import BeautifulSoup

webcontent = requests.get('http://www.mtsu.edu')

webcontent_soup = BeautifulSoup(webcontent.text, 'html.parser')

webcontent_links = webcontent_soup.find_all('a')

for link in webcontent_links:
    print(link)

    print()
