from datetime import datetime
from database.connect import area_cause,area,daily,monthly,weekly
from utils.date_utils import get_week_range,get_month_range


def find_number_accident_by_area_and_time(area_code: str, date: datetime):
    convert_to_start_week = get_week_range(date)[0]
    convert_to_month, convert_to_year = get_month_range(date)[0], get_month_range(date)[1]

    return {'accidents in day': find_number_accident_at_day(date, area_code),
            'accident in week': find_number_accident_at_week(convert_to_start_week, area_code),
            'accident in month': find_number_accident_at_month(convert_to_month,
                                                               convert_to_year, area_code)

            }

def find_number_accident_at_day(date: datetime, area_code: str):
     return list(daily.find(
         { 'date': date, 'beat_of_occurrence': area_code },
         {
             '_id': 0,
         }
     ))

def find_number_accident_at_week(start_week: str, area_code: str):
     return list(weekly.find(
         { 'start_week': start_week, 'beat_of_occurrence': area_code },
         {
             '_id': 0
         }
     ))

def find_number_accident_at_month(month: str, year: str, area_code: str):
     return list(monthly.find(
         { 'month': month, 'year': year, 'beat_of_occurrence': area_code },
         {
             '_id': 0
         }
     ))

def find_injuries_by_area(area_code: str):
    all_injuries = list(area.aggregate([
        {'$lookup': { 'from': 'accidents', 'localField': 'crash_id',
                      'foreignField': 'crash_id', 'as': 'accidents'}},
        {'$match': { 'beat_of_occurrence': area_code } },
        {'$project': {
            'beat_of_occurrence': 1,
            'injuries.total': 1,
            'injuries.fatal': 1,
            'injuries.incapacitating': 1,
            'injuries.non_incapacitating': 1,
            'accidents': 1,
            '_id': 0
        } }
    ]))

    for injury in all_injuries:
        for accident in injury['accidents']:
            accident['_id'] = str(accident['_id'])

    return all_injuries

def find_number_accident_by_area(area_code: str):
    all_accidents = list(area.find(
        {'beat_of_occurrence': area_code},
        {
            'beat_of_occurrence': 1,
            'sum_accident': 1,
            '_id': 0
        }
    ))
    return all_accidents


def find_accidents_by_area_filter_cause(area_code: str):
    all_injuries = list(area_cause.find(
        {'beat_of_occurrence': area_code},
        {
            'prim_contributory_cause': 1,
            'injuries.total': 1,
            'injuries.fatal': 1,
            'injuries.incapacitating': 1,
            'injuries.non_incapacitating': 1,
            '_id': 0
        }
    ))
    return all_injuries

