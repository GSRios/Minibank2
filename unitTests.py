import unittest
from domain.client import Client
from domain.account import Account
import uuid

class ClientTest(unittest.TestCase):
    def test_create_client(self):
        c = Client()
        c.create_client('testName', 'test@email.com')
        self.assertEquals(len(c.changes), 1)


    def test_load_client(self):
        c = Client()
        c.create_client('testName', 'test@email.com')
        load_client = Client(c.changes)
        self.assertEquals(load_client.id, c.id)


    def test_create_account(self):
        a = Account()
        a.create_account(uuid.uuid4())
        self.assertEquals(len(a.changes), 1)
        self.assertEquals(a.balance, 0)


    def test_load_account(self):
        a = Account()
        a.create_account(uuid.uuid4())
        a.make_deposit(20)
        load_acc = Account(a.changes)
        self.assertEquals(load_acc.balance, 20)
        self.assertEquals(load_acc.id, a.id)


    def test_deposit(self):
        a = Account()
        a.create_account(uuid.uuid4())
        a.make_deposit(50)
        self.assertEquals(len(a.changes), 2)
        self.assertEquals(a.balance, 50)


    def test_withdrawal(self):
        a = Account()
        a.create_account(uuid.uuid4())
        a.make_withdrawal(50)
        self.assertEquals(len(a.changes), 2)
        self.assertEquals(a.balance, -50)   


    def test_withdrawal_deposit(self):
        a = Account()
        a.create_account(uuid.uuid4())
        a.make_deposit(500)
        a.make_deposit(20)
        a.make_withdrawal(50)
        a.make_deposit(5000)
        a.make_withdrawal(100)
        self.assertEquals(len(a.changes), 6)
        self.assertEquals(a.balance, 5370)

if __name__ == '__main__':
    unittest.main()        