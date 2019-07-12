import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['ptt_crawler_db']
collection = db['ptt_crawler_collection']

for data in collection.find():
    print('title: '+data['title'])
    print('url: '+data['url'])
    print('content: '+data['content'][:60])
    print()
