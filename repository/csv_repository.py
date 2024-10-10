import csv
import os


from database.connect import taxi_db, drivers, cars


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

def init_taxi_drivers():
   drivers.drop()
   cars.drop()

   path = os.path.join(os.path.dirname(__file__), '..', 'data', 'practice_data.csv')
   for row in read_csv(path):
       car = {
           'license_id': row['CarLicense'],
           'brand': row['CarBrand'],
           'color': row['CarColor']
       }


       car_id = cars.insert_one(car).inserted_id


       address = {
           'city': row['City'],
           'street': row['Street'],
           'state': row['State']
       }


       driver = {
           'passport': row['PassportNumber'],
           'first_name': row['FullName'].split(' ')[0],
           'last_name': row['FullName'].split(' ')[1],
           'car_id': car_id,
           'address': address
       }


       drivers.insert_one(driver)