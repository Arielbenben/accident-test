from datetime import datetime
from flask import Blueprint, jsonify, request

from database.connect import area_cause
from repository.database_repository import init_database
from repository.statistics_repository import (find_number_accident_by_area,
                                              find_number_accident_by_area_and_time,
                                              find_accidents_by_area_filter_cause, find_injuries_by_area)


statistic_accident_blueprint = Blueprint('statistic', __name__)


@statistic_accident_blueprint.route('/init', methods=['POST'])
def init_data_db_route():
    try:
        init_database()
        return jsonify({'message': 'database and indexes created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_accident_blueprint.route('/accident_area/<string:area_code>', methods=['GET'])
def find_number_accident_in_area_route(area_code:str):
    try:
        number_accident = find_number_accident_by_area(area_code)
        return jsonify(number_accident), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


@statistic_accident_blueprint.route('/area_time/<string:area_code>', methods=['GET'])
def find_number_accident_in_area_in_specific_time_route(area_code: str):
    try:
        date = request.args.get('date', type=str)
        convert_to_date = datetime.strptime(date, '%m/%d/%Y')
        number_accident = find_number_accident_by_area_and_time(area_code, convert_to_date)
        return jsonify(number_accident), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


@statistic_accident_blueprint.route('/group_cause/<string:area_code>', methods=['GET'])
def get_accidents_group_by_cause_route(area_code: str):
    try:
        group_by_cause = find_accidents_by_area_filter_cause(area_code)
        return jsonify(group_by_cause), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


@statistic_accident_blueprint.route('/injuries_area/<string:area_code>', methods=['GET'])
def get_injuries_in_area_route(area_code: str):
    try:
        all_injuries = find_injuries_by_area(area_code)
        return jsonify(all_injuries), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500