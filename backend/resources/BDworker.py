from flask import jsonify, make_response, send_file
from flask_restful import Resource


class BDworker(Resource):
    # PAGE - http://localhost:3000/data
    def get(self):
        return send_file('relations.json', as_attachment=True)

    # not tested
    def post(self):
        return make_response(
            jsonify({}),
            201)

