from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from controllers.statcontroller import get_stat_info

parser = reqparse.RequestParser()
parser.add_argument('category', location='args')

categories = {0: (3, 3), 1: (2, 2), 2: (0, 1), 3: (0, 3)}


class Stat(Resource):
    # PAGE - http://localhost:3000/data
    def get(self):
        args = parser.parse_args()
        category = int(args.get("category"))
        if category not in categories.keys():
            return make_response(
                jsonify([{'error': 'Unknown category'}]),
                200)
        result = get_stat_info(categories[category])
        return make_response(
            jsonify(result),
            200)

