from celery import Celery
import requests
from bs4 import BeautifulSoup
import re
app = Celery('tasks')

home_url = 'https://www.ptt.cc'
@app.task
def crawler():
    url = 'https://www.ptt.cc/bbs/forsale/index.html'
    page.delay(url)
    page_number = int( re.search(r'index(\d+)', doc.select('a.btn.wide')[1]['href']).group(1) )
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    for pg in range(page_number, page_number-3, -1):
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
    print( data['url'] )
