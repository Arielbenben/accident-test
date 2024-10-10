import pytest
from flask import Flask
from controllers.statistic_accident_controller import statistic_accident_blueprint


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(statistic_accident_blueprint)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_init_data_db_route(client):
    response = client.post('/init')
    assert response.status_code == 201


def test_find_number_accident_in_area_route(client):
    response = client.get('/accident_area/225')
    assert response.status_code == 200


def test_find_number_accident_in_area_in_specific_time_route(client):
    response = client.get('/area_time/225?date=09/05/2023')
    assert response.status_code == 200


def test_get_accidents_group_by_cause_route(client):
    response = client.get('/group_cause/225')
    assert response.status_code == 200


def test_get_injuries_in_area_route(client):
    response = client.get('/injuries_area/225')
    assert response.status_code == 200

