from flask import jsonify, make_response, send_file, request
from flask_restful import Resource
from controllers.exportcontroller import export_data_base
from controllers.importcontroller import import_collection


class BDworker(Resource):
    # PAGE - http://localhost:3000/data
    def get(self):
        file = export_data_base()
        return send_file(file, as_attachment=True)

    # not tested
    def post(self):
        filename = list(request.files)[0]
        file = request.files[filename]
        data = file.read()
        print('fileName - ' + filename)
        file.save(filename)
        res = import_collection(filename, data)
        if res is None:
            return make_response( jsonify({'status': 'ok'}), 201)
        else:
            return make_response(
                jsonify(res),
                201)

