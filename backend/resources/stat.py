from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response, send_file

parser = reqparse.RequestParser()
parser.add_argument('way_id', location='args')
parser.add_argument('min_jam', location='args')
parser.add_argument('max_jam', location='args')


class Stat(Resource):
    # PAGE - http://localhost:3000/data
    def get(self):
        args = parser.parse_args()
        way_id = int(args.get("way_id"))
        min_jam = int(args.get("min_jam"), 0)
        return make_response(
            jsonify({}),
            200)

