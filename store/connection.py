import psycopg2

class Connection(object):   
    def get_connection(self):
        conn = None
        conn = psycopg2.connect(dbname='minibank', user='usr', host='localhost', password='pass')
        return conn