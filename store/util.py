from base import Store
from base import EventStream
from base import EventStore
from connection import Connection


def store():
    conn = Connection()
    store = Store(conn.get_connection())
    event_store = EventStore(store)
    return event_store