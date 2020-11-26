from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from controllers.waycontroller import get_ways_info

parser = reqparse.RequestParser()
parser.add_argument('way_id', location='args')
parser.add_argument('min_jam', location='args')
parser.add_argument('max_jam', location='args')


class Ways(Resource):
    # PAGE - http://localhost:3000/traffic
    def get(self):
        args = parser.parse_args()
        name = args.get("name")
        min_jam = int(args.get("min_jam"), 0)
        max_jam = int(args.get("max_jam"), 3)
        result = get_ways_info(min_jam, max_jam, name)
        return make_response(
            jsonify(result),
            200)
