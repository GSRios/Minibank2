import pickle
import psycopg2

class Store(object):
    def __init__(self, conn):
        self.conn = conn
    

    def insert(self, id, data):
        c = self.conn.cursor()
        version_query = """
        SELECT COALESCE(MAX(version), 0)
        FROM public.events
        WHERE id_event = %(id)s
        """        
        c.execute(version_query,{'id':  str(id)})
        (version,) = c.fetchone()

        version += 1
        insert_query = """
        INSERT INTO public.events (id_event, version, data)
        VALUES ( %(id)s, %(version)s, %(data)s)
        """    
        c.execute(insert_query, {'id' : str(id), 'version': int(version), 'data': psycopg2.Binary(data)})      
        self.conn.commit()
        c.close()
        
    

    def fetchone(self, id):        
        c = self.conn.cursor()
        sql = """
        SELECT DATA, VERSION FROM EVENTS
        WHERE id_event = %(id)s 
        ORDER BY VERSION       
        """
        c.execute(sql, {'id': id})

        for row in c.fetchall():
            data, version = row
            yield {'version': version, 'data': data}        

        c.close()


    def close(self):
        self.conn.close()



class EventStream(object):
    def __init__(self, version=-1, events=None):
        self.version = version
        if events is None:
            self.events = []
        else:
            self.events = list(events)



class EventStore(object):
    def __init__(self, store):
        self.store = store


    def save(self, id_event, events):
        data = self.serialize_event(events)
        self.store.insert(id_event, data)


    def load(self, id_event, max_count=1):
        records = self.store.fetchone(id_event)
        stream = EventStream()
        for record in records:
            stream.events.extend(self.deserialize_event(record['data']))
            stream.version = record['version']
        return stream

    def serialize_event(self, event):
        return pickle.dumps(event)


    def deserialize_event(self, event):
        return pickle.loads(event)