from bs4 import BeautifulSoup
import requests
import csv

source  = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('ex_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


# this is where we got the entire element that housed the 'article' id/class
for article in soup.find_all('article'):
#print(article.prettify())

# this is where we go the headline
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    '''
    vid_src = article.find('iframe', class_='youtube-player')['src']
    # print(vid_src)

    # this is to get something specific from the video link
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    # print(vid_id)

    # format string
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)
    '''

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

    csv_file.close()







