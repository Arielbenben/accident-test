from pymongo import MongoClient


client = MongoClient('mongodb://172.19.191.59:27017')
taxi_db = client['taxi-drivers']


drivers = taxi_db['drivers']
cars = taxi_db['cars']

customers = taxi_db['customers']
products = taxi_db['products']
invoices = taxi_db['invoices']


