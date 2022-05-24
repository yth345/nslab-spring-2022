from sys import argv
from pymongo import MongoClient
from pprint import pprint 
import csv
import numpy as np
import matplotlib.pyplot as plt

client = MongoClient('localhost:25555')
db = client.Twitch
serverStatusResult = db.command('serverStatus')


##### get document count in all collections #####
doc_cnt = dict()
for c_name in db.list_collection_names():
    cnt = db[c_name].count_documents({})
    doc_cnt[c_name] = cnt
pprint(doc_cnt)


'''
result: 20 collections
{'Taiwan': 44960, 
 'Russian': 35876, 
 'Brazil': 79405, 
 'Ukraine': 162506, 
 'South_Korea': 42156, 
 'Spain': 73729, 
 'United_Kingdom': 183635, 
 'Canada': 137927, 
 'France': 171046, 
 'Netherlands': 140551, 
 'Germany': 124287, 
 'Japan': 67773, 
 'Australia': 64641, 
 'Denmark': 71444, 
 'Poland': 72090, 
 'Sweden': 60249, 
 'Italy': 79485, 
 'Turkey': 69502, 
 'United_States': 284249, 
 'SouthKorea': 19350}
'''


##### get the first document in collection['Taiwan'] #####
pprint(db.Taiwan.find_one())

'''
TW result:
{'_id': ObjectId('5f8dfd6444f5020110f893a7'),
 'channel': 'klean',
 'end': '2020-10-19T20:56:04',
 'language': 'en',
 'serverPool': ['52.223.247.211', '45.113.128.160'],
 'start': '2020-10-19T14:56:04',
 'transactionList': {'2020-10-19T14:56:08': '52.223.247.211',
                     '2020-10-19T14:59:24': '52.223.247.211',
                     '2020-10-19T15:00:34': '52.223.247.211',
                     '2020-10-19T15:02:04': '45.113.128.160',
                     '2020-10-19T15:04:46': '45.113.128.160',
                        ...
                     '2020-10-19T20:41:15': '45.113.128.160',
                     '2020-10-19T20:44:40': '52.223.247.211',
                     '2020-10-19T20:47:33': '45.113.128.160',
                     '2020-10-19T20:52:11': '45.113.128.160',
                     '2020-10-19T20:54:24': '52.223.247.211'}}
'''


##### write all the documents in collection to .csv #####

with open('tw_docs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'channel', 'language', 'start', 'end', 'serverPool'])
    for doc in db.Taiwan.find({}, {'_id':1, 'channel':1, 'language':1, 'start':1, 'end':1, 'serverPool':1}):
        new_row = [doc['_id'], doc['channel'], doc['language'], doc['start'], doc['end']]
        if 'serverPool' in doc:
            new_row.append(doc['serverPool'])
        else:
            new_row.append('')
        writer.writerow(new_row)


##### check the all the columns in collection #####
'''
with open('docs_raw.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for doc in db.Turkey.find():
        writer.writerow(doc)
'''

