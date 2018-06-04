class AccountCreated(object):
    def __init__(self, id, client_id):
        self.id = id
        self.client_id = client_id




class DepositPerformed(object):
    def __init__(self, amount):
        self.amount = amount




class WithdrawalPerformed(object):
    def __init__(self, amount):
        self.amount = amount