from datetime import datetime
from repository.statistics_repository import find_number_accident_by_area_and_time, find_injuries_by_area, \
                                             find_number_accident_by_area, find_accidents_by_area_filter_cause



def test_find_number_accident_by_area_and_time():
   result = find_number_accident_by_area_and_time('225', datetime(2023, 10, 5))
   assert len(result) > 0


def test_find_injuries_by_area():
   result = find_injuries_by_area('225')
   assert len(result) > 0


def test_find_number_accident_by_area():
   result = find_number_accident_by_area('225')
   assert len(result) > 0


def test_find_accidents_by_area_filter_cause():
   result = find_accidents_by_area_filter_cause('225')
   assert len(result) > 0

