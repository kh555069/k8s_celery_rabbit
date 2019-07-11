from celery import Celery
import requests
from bs4 import BeautifulSoup
import re
import pymongo
app = Celery('tasks')

home_url = 'https://www.ptt.cc'
# connect to mongodb
client = pymongo.MongoClient('localhost', 27017)
db = client['ptt_crawler_db']
collection = db['ptt_crawler_collection']

@app.task
def crawler():
    url = 'https://www.ptt.cc/bbs/forsale/index.html'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    page_number = int( re.search(r'index(\d+)', soup.select('a.btn.wide')[1]['href']).group(1) )

    for pg in range(page_number+1, page_number-3, -1):
        page_url = home_url + '/bbs/forsale/index{}.html'.format(pg)
        page.delay(page_url)

@app.task
def page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    items=[]
    for ele in soup.select('.r-ent'):
        data={}
        data['title'] = ele.select('.title')[0].text
        data['url'] = home_url + ele.select('.title a')[0]['href']
        article.delay(data)

@app.task
def article(data):
    item_res = requests.get( data['url'] )
    item_soup = BeautifulSoup(item_res.text, 'lxml')
    data['content'] = item_soup.select('#main-content')[0].text.strip()
    print( data['title'] )
    collection.insert_one(data)
