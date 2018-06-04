import uuid
class ClientJoined(object):
    def __init__(self, name, email):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        