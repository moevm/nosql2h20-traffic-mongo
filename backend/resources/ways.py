from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response

parser = reqparse.RequestParser()
parser.add_argument('way_id', location='args')
parser.add_argument('min_jam', location='args')
parser.add_argument('max_jam', location='args')


class Ways(Resource):
    # PAGE - http://localhost:3000/traffic
    def get(self):
        args = parser.parse_args()
        way_id = int(args.get("way_id"))
        min_jam = int(args.get("min_jam"), 0)
        max_jam = int(args.get("max_jam"), 10)
        result = [
            {
                "id": way_id,
                "coordinate": {
                    "x": 2,
                    "y": 1
                },
                "traffic_jam_level": 1
            },
            {
                "id": way_id + 1,
                "coordinate": {
                    "x": 23,
                    "y": 12
                },
                "traffic_jam_level": 6
            }
        ]
        return make_response(
            jsonify(result),
            200)
