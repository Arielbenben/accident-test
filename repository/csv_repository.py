import csv
import os
from database.connect import daily,weekly, monthly,area,accidents,area_cause
from utils.date_utils import convert_to_date,get_week_range,get_month_range,convert_to_int


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

def init_accidents_db():
    if accidents.count_documents({}) > 0:
        return

    accidents.drop()
    daily.drop()
    weekly.drop()
    monthly.drop()
    area.drop()


    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')
    for row in read_csv(data_path):

       converted_to_date = convert_to_date(row['CRASH_DATE'])

       accident = {
           'crash_id': row['CRASH_RECORD_ID'],
           'crash_date': converted_to_date,
           'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
           'injuries': {
               'total': row['INJURIES_TOTAL'],
               'fatal': row['INJURIES_FATAL'],
               'incapacitating': row['INJURIES_INCAPACITATING'],
               'non_incapacitating': row['INJURIES_NON_INCAPACITATING']
           },
           'cause': {
               'prim_contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
               'set_contributory_cause': row['SEC_CONTRIBUTORY_CAUSE']
           }
       }

       accidents.insert_one(accident)

       daily.update_one(
           {'date': converted_to_date,
            'beat_of_occurrence': row['BEAT_OF_OCCURRENCE']},
           {
               '$inc': {'sum_accident': 1}
           },

           upsert=True
       )

       start_week = get_week_range(converted_to_date)[0]
       end_week = get_week_range(converted_to_date)[1]

       weekly.update_one(
           {'start_week': start_week, 'end_week': end_week,
            'beat_of_occurrence': row['BEAT_OF_OCCURRENCE']},
           {
               '$inc': {'sum_accident': 1}
           },
           upsert=True
       )

       convert_to_month = get_month_range(converted_to_date)[0]
       convert_to_year = get_month_range(converted_to_date)[1]

       monthly.update_one(
           {'month': convert_to_month, 'year': convert_to_year,
            'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'], },
           {
               '$inc': {'sum_accident': 1}
           },

           upsert=True
       )

       area_cause.update_one(
           {'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
            'prim_contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE'] },
           {
               '$inc': {
                   'sum_accident': 1,
                   'injuries.total': convert_to_int(row['INJURIES_TOTAL']),
                   'injuries.fatal': convert_to_int(row['INJURIES_FATAL']),
                   'injuries.incapacitating': convert_to_int(row['INJURIES_INCAPACITATING']),
                   'injuries.non_incapacitating': convert_to_int(row['INJURIES_NON_INCAPACITATING']),
               },
               '$push': {'crash_id': row['CRASH_RECORD_ID']}
           },
           upsert=True
       )

       area.update_one(
           { 'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'] },
           {
               '$inc': {
                   'sum_accident': 1,
                   'injuries.total': convert_to_int(row['INJURIES_TOTAL']),
                   'injuries.fatal': convert_to_int(row['INJURIES_FATAL']),
                   'injuries.incapacitating': convert_to_int(row['INJURIES_INCAPACITATING']),
                   'injuries.non_incapacitating': convert_to_int(row['INJURIES_NON_INCAPACITATING']),
               },
               '$push': {'crash_id': row['CRASH_RECORD_ID']}
           },
           upsert=True
       )


init_accidents_db()





