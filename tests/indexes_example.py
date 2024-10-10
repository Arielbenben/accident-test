from repository.database_repository import create_indexes


def without_indexes():
    area.create_index({'beat_of_occurrence': 1, 'prim_contributory_cause': 1})
    daily.create_index({'beat_of_occurrence': 1, 'crash_date': 1})
    weekly.create_index({'beat_of_occurrence': 1, 'start_week': 1, 'end_week': 1})
    monthly.create_index({'beat_of_occurrence': 1, 'month': 1, 'year': 1})

    print()
    return



def after_indexes():
    create_indexes()
    print()
    return
