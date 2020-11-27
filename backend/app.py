import os
from flask import Flask
from flask_restful import Api
from resources.apimap import ApiMap
from resources.ways import Ways
from resources.BDworker import BDworker as bd
from resources.stat import Stat
from utils.traffic_update import start_updating_thread

app = Flask(__name__)
api = Api(app)

api.add_resource(ApiMap, '/map')
api.add_resource(Ways, '/way')
api.add_resource(bd, '/bd')
api.add_resource(Stat, '/stat')

if __name__ == "__main__":
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        second_thread = start_updating_thread()
    app.run(port=5000, host='0.0.0.0', debug=True)
