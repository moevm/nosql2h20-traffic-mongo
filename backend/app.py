from flask import Flask
from flask_restful import Api
from resources.apimap import ApiMap

app = Flask(__name__)
api = Api(app)

api.add_resource(ApiMap, '/map')

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)
