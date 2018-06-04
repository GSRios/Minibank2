from flask import Flask
from flask_restful import Api
from resource import ClientIncomingResource
from resource import ClientOutgoingResource
from resource import AccountIncomingResource
from resource import AccountOutgoingResource
from resource import DepositResource
from resource import WithdrawalResource
from resource import TransactionOutgoingResource


class Application(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(ClientIncomingResource, '/client', endpoint='clients')
        self.api.add_resource(ClientOutgoingResource, '/client/<string:id>', endpoint='client')
        self.api.add_resource(AccountIncomingResource, '/account', endpoint='accounts')
        self.api.add_resource(AccountOutgoingResource, '/account/<string:id>', endpoint='account')
        self.api.add_resource(DepositResource, '/account/<string:account_id>/deposit')
        self.api.add_resource(WithdrawalResource, '/account/<string:account_id>/withdrawal')
        self.api.add_resource(TransactionOutgoingResource, '/account/<string:account_id>/history')

    
    def run(self):
        self.app.run(port=5000)

app = Application()
app.run()
