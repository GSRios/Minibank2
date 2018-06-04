from flask_restful import Resource, reqparse
from flask import request, url_for, jsonify
from service.client import Service

class ClientIncomingResource(Resource):               
    def __init__(self):       
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
            type=str,
            required=True,
            help="This field cannot be empty"
        )
        self.parser.add_argument('email',
            type=str,
            required=True,
            help="This field cannot be empty"
        )   
      
   
    def post(self):        
        data = self.parser.parse_args()       
        client_id = Service.process_client(**data)
        return url_for('client', id=client_id), 201