import requests
import unicodedata
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://lindajuliano.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='content')

posts = results.find_all('article', class_='post-wrapper')

for post in posts:
   title = post.find('h1')
   content = post.find_all('p')
   post_title = title.text
   x = unicodedata.normalize('NFKD', post_title).encode('ascii','ignore')
   final_title = x.replace(" ","-").lower()

   date = post.find('time')
   time = date['datetime']
   date_only = time[0:10]
   date_item = unicodedata.normalize('NFKD', date_only).encode('ascii','ignore')

   # f = open("linda_blog/_posts/%s-%s.md" % (date_item, final_title), "w")
   # f.write("---\nlayout: post\ntitle:  %s\ndate:   %s 12:00:00 -0700\ntags: tag\nsummary: 'This is a post'\ntagline: 'tagline here'\n---\n" % (x, date_item))
   # f.write("\n%s" % content)
   # f.close

   print(final_title)
   print(type(final_title))