from domain.client import Client
from store import Store
from store import EventStream
from store import EventStore
from store import Connection
from store import store
from service.exception import ClientNotFoundException

class Service(object):


    @staticmethod
    def process_client(name, email):      
        event_store = store()
        
        client = Client()
        client.create_client(name, email)
        event_store.save(client.id, client.changes)        
        return client.id

    @staticmethod
    def get(id):        
        event_store = store()

        stream = event_store.load(id)
        if stream.version == -1:
            raise ClientNotFoundException(id)
        acc = Client(stream.events)
        json_acc = {'name': acc.name, 'email': acc.email}
        return json_acc


    
