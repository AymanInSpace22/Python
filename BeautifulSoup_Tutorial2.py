from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# prettify() will allow for indentation in the console
#print(soup.prettify())

match = soup.title.text
print(match)

# this is to search for a specific element. It goes based on classe's and id's. The class has an 
# underscore becuase the word class is a keyword in Python
# if you were searching for an id, then it would just be id=''
'''
article = soup.find('div', class_='article') # find method takes 2 arguments
print(article)

headline = article.h2.a.text
print(headline)
summary = article.p.text
print(summary)
'''

# this will allow us to loop though all elements with the article class
for article in soup.find_all('div', class_='article'): # find method takes 2 arguments
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)

    print()
