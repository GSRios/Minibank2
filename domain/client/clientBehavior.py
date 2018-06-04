from domain import Mix

class ClientState(Mix):

    def clientjoined(self, event):
        self.id = event.id
        self.name = event.name
        self.email = event.email