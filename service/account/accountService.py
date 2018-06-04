from domain.account import Account
from domain.account import DepositPerformed
from domain.account import WithdrawalPerformed
from service.exception import AccountNotFoundException
from service.exception import ClientNotFoundException
from store import store
import smtplib
import re
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class Service(object):    
    def process_account(self, client_id):        
        event_store = store()
        client_stream = event_store.load(client_id)
        if client_stream.version == -1:
            raise ClientNotFoundException(client_id)
        account = Account()
        account.create_account(client_id)
        event_store.save(account.id, account.changes) 
        #self.send_email(account.id)       
        return account.id


    def get_events(self, id):
        event_store = store()
        stream = event_store.load(id)
        if -1 == stream.version:
            raise AccountNotFoundException(id)
        return stream.events


    def get(self,id):                    
        acc = Account(self.get_events(id))
        json_acc = {'balance': float(acc.balance)}
        return json_acc


    
    def deposit(self, amount, id):          
        if amount < 0:
            raise ValueError('Invalid amount.')        
        acc = Account(self.get_events(id))
        acc.make_deposit(amount)
        event_store = store() 
        event_store.save(acc.id, acc.changes)  


    
    def withdrawal(self,amount, id):       
        if amount < 0:
            raise ValueError('Invalid amount.')        
        acc = Account(self.get_events(id))        
        if acc.balance - amount < 0:
            raise ValueError('You don\'t have that amount to withdrawal.')
        acc.make_withdrawal(amount)
        event_store = store() 
        event_store.save(acc.id, acc.changes) 


    
    def get_history(self, id): 
        events = self.get_events(id)
        history = [{'Transaction': re.findall('[A-Z][^A-Z]*', type(event).__name__)[0], 
                    'Value': float(event.amount)
                    }
            for event in events if type(event) is DepositPerformed or type(event) is WithdrawalPerformed
        ]       
        return history


    def send_email(self, id):
        from_addr = 'minibanksystem@gmail.com'
        to_addr = 'cfo@email.com'
        msg = MIMEMultipart()
        msg['from'] = from_addr
        msg['to'] = to_addr
        msg['subject'] = 'A new account has been created'

        body = 'Hello! A customer create a new account with the following identification {}'.format(id)
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, 'password to email (minibanksystem)')
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()
