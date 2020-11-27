from flask_restful import Resource
from flask import jsonify, make_response
from controllers.statcontroller import get_stat_info


class Stat(Resource):
    # PAGE - http://localhost:3000/data
    def get(self):
        result = get_stat_info()
        return make_response(
            jsonify(result),
            200)

