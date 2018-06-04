from domain import Mix

class AccountState(Mix):

    def accountcreated(self, event):
        self.id = event.id
        self.client_id = event.client_id
        self.balance = 0


    def depositperformed(self, event):
        self.balance += event.amount

    
    def withdrawalperformed(self, event):
        self.balance -= event.amount
