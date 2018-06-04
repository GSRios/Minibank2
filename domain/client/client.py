from clientBehavior import ClientState
from clientEvents import ClientJoined
from domain.changes import Changes


class Client(ClientState, Changes):
    def create_client(self, name, email):
        create_client_event = ClientJoined(name, email)
        self.apply(create_client_event)