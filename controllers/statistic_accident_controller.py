from flask import Blueprint, jsonify, request
from database.connect import accidents,daily,monthly,weekly,area
from repository.database_repository import init_database
from repository.statistics_repository import find_number_accident_by_area

statistic_accident_blueprint = Blueprint('statistic_accident', __name__)


@statistic_accident_blueprint.route('/', methods=['POST'])
def init_data_db_route():
    try:
        init_database()
        return jsonify({'message': 'database and indexes created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_accident_blueprint.route('/<string:area_code>', methods=['GET'])
def find_number_accident_in_area(area_code:str):
    try:
        number_accident = find_number_accident_by_area(area_code)
        return jsonify(number_accident), 200
    except Exception as e:
     return jsonify({'Error': str(e)}), 500


@statistic_accident_blueprint.route('/<string:area_code>', methods=['GET'])
def find_number_accident_in_area(area_code:str):
    try:
        number_accident = find_number_accident_by_area(area_code)
        return jsonify(number_accident), 200
    except Exception as e:
     return jsonify({'Error': str(e)}), 500