from accountBehavior import AccountState
from domain.changes import Changes
from accountEvents import AccountCreated
from accountEvents import DepositPerformed
from accountEvents import WithdrawalPerformed
import uuid

class Account(AccountState, Changes):
    def create_account(self, client_id):
        account_created_event = AccountCreated(uuid.uuid4(), client_id)
        self.apply(account_created_event)

    def make_deposit(self, amount):    
        deposit_event = DepositPerformed(amount)
        self.apply(deposit_event)
    

    def make_withdrawal(self, amount):
        withdrawal_event = WithdrawalPerformed(amount)
        self.apply(withdrawal_event)