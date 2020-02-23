import json
from flask import make_response
from flask_restful import Resource

def output_json(data, code, headers=None):
    """Makes a response with a JSON encoded body"""
    response = make_response(json.dumps(data), code)
    response.headers.extend(headers or {})
    return response


class ResourceView(Resource):
    def __init__(self, db, parser):
        self.db = db
        self.parser = parser
        self.representations = {
            'application/json': output_json
        }