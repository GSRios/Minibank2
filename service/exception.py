class AccountNotFoundException(Exception):
    def __init__(self, id):
        super(AccountNotFoundException, self).__init__('Account with the following ID not found: {}'.format(id))        


class ClientNotFoundException(Exception):
    def __init__(self, id):
        super(ClientNotFoundException, self).__init__('Client with the following ID not found: {}'.format(id))