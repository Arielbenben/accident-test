from flask import Blueprint, jsonify, request
from database.connect import accidents,daily,monthly,weekly,area
from repository.database_repository import init_database

statistic_accident_blueprint = Blueprint('statistic_accident', __name__)


@statistic_accident_blueprint.route('/', methods=['POST'])
def init_data_db_route():
    try:
        init_database()
        return jsonify({'message': 'database and indexes created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@statistic_accident_blueprint.route('/', methods=['POST'])
def create_index_db_route():
    try:
        car = get_car_by_id(c_id, cars)
        if car:
            return jsonify(car), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500