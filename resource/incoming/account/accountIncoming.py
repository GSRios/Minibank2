from flask_restful import Resource, reqparse
from flask import request, url_for, jsonify
from service.account import Service
from service.exception import ClientNotFoundException
from service.exception import AccountNotFoundException

class AccountIncomingResource(Resource):
    def __init__(self):         
        self.service = Service()      
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('client_id',
            type=str,
            required=True,
            help="This field cannot be empty"
        ) 
   

    def post(self):
        data = self.parser.parse_args()
        try:
            account_id = self.service.process_account(data['client_id'])
        except ClientNotFoundException as ex:
            return {'Message' : str(ex)}, 404
        except Exception as e:
            return {'Message' : 'An error ocurred'}, 404
        return url_for('account', id=account_id), 201




class DepositResource(Resource):
    def __init__(self):              
        self.service = Service()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('amount',
            type=float,
            required=True,
            help='This field cannot be empty'
        ) 
    
    def post(self, account_id):
        data = self.parser.parse_args()
        amount = data['amount']
        try:
            self.service.deposit(amount, account_id)
        except ValueError as value_error:
            return {'Message': str(value_error)}, 403
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found)}, 404    
        return {"Message":"Transaction completed with success"}




class WithdrawalResource(Resource):

    def __init__(self):
        self.service = Service()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('amount',
            type=float,
            required=True,
            help='This field cannot be empty'
        ) 
    
    def post(self, account_id):       
        data = self.parser.parse_args()
        amount = data['amount']
        try:
            self.service.withdrawal(amount, account_id)      
        except ValueError as value_error:
            return {'Message': str(value_error)}, 403
        except AccountNotFoundException as account_not_found:
            return {'Message': str(account_not_found) }, 404    
        return {"Message":"Transaction completed with success"}        