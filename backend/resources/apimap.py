from flask_restful import reqparse, abort, Resource
from controllers.mapcontroller import find_paths_from_one_point_to_another_point
from flask import jsonify, make_response

parser = reqparse.RequestParser()
parser.add_argument('lon_from', location='args')
parser.add_argument('lon_to', location='args')
parser.add_argument('lat_to', location='args')
parser.add_argument('lat_from', location='args')


class ApiMap(Resource):
    
    def get(self):
        args = parser.parse_args()
        lon_from = float(args.get("lon_from"))
        lat_from = float(args.get("lat_from"))
        lon_to = float(args.get("lon_to"))
        lat_to = float(args.get("lat_to"))
        demo_answer = [
        {
            "way": [
                [59.9190, 30.3078], [lon_to, lat_to-0.001]
                ]
        }
        ]
        return make_response(
        jsonify({"path": demo_answer}),
         200)
        '''
        #json.dumps({"path": demo_answer})
        #return json.dumps(find_paths_from_one_point_to_another_point(
        #    lon_from,
        #    lat_from,
        #    lon_to,
        #    lat_to
        #))
        '''
