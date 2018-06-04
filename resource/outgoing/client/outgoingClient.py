from flask_restful import Resource, reqparse
from flask import request, url_for, jsonify
from service.client import Service
from service.exception import ClientNotFoundException

class ClientOutgoingResource(Resource):
    def get(self, id):
        try:        
            acc = Service.get(id)            
        except (KeyError, ClientNotFoundException) as ex:
            return {'Message': str(ex)}, 404
        return jsonify(acc)