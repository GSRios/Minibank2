from flask_restful import Resource, reqparse
from flask import request, url_for, jsonify
from service.account import Service
from service.exception import AccountNotFoundException

class AccountOutgoingResource(Resource):
    def get(self, id):
        try:      
            service = Service()  
            acc = service.get(id)           
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404
        return jsonify(acc)