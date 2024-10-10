from repository.csv_repository import init_accidents_db
from database.connect import area,daily,weekly,monthly


def init_database():
    init_accidents_db()
    create_indexes()
    return


def create_indexes():
    area.create_index({'beat_of_occurrence': 1, 'prim_contributory_cause': 1 } )
    daily.create_index( { 'beat_of_occurrence': 1, 'crash_date': 1 } )
    weekly.create_index( { 'beat_of_occurrence': 1, 'start_week': 1, 'end_week': 1 } )
    monthly.create_index({'beat_of_occurrence': 1, 'month': 1, 'year': 1 } )
    return
