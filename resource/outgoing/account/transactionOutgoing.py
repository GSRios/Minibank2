from flask_restful import Resource, reqparse
from flask import request, url_for, jsonify
from service.account import Service

class TransactionOutgoingResource(Resource):
    def get(self, account_id):
        try:       
            service = Service() 
            acc = service.get_history(account_id)            
        except (KeyError) as ex:
            return {'Message': str(ex)}, 404
        return jsonify(acc)