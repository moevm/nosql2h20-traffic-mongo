from flask import jsonify, make_response, send_file, request
from flask_restful import Resource
from controllers.exportcontroller import export_data_base


class BDworker(Resource):
    # PAGE - http://localhost:3000/data
    def get(self):
        file = export_data_base()
        return send_file(file, as_attachment=True)

    # not tested
    def post(self):
        filename = list(request.files)[0]
        file = request.files[filename]
        print('fileName - ' + filename)
        file.save(filename)
        return make_response(
            jsonify({}),
            201)

