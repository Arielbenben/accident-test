from flask import Flask
from controllers.statistic_accident_controller import statistic_accident_blueprint


app = Flask(__name__)

app.register_blueprint(statistic_accident_blueprint, url_prefix='/api/statistic')

if __name__ == '__main__':
    app.run(debug=True)