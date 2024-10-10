from pymongo import MongoClient


client = MongoClient('mongodb://172.19.191.59:27017')
accidents_db = client['accidents']


accidents = accidents_db['accidents']
daily = accidents_db['daily']
weekly = accidents_db['weekly']
monthly = accidents_db['monthly']
area = accidents_db['area']
area_cause = accidents_db['area_cause']





