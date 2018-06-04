from mix import Mix

class Changes(Mix):
    def __init__(self, *args, **kwargs):
        super(Changes, self).__init__(*args, **kwargs)
        self.changes = []


    def apply(self, event):
        self.changes.append(event)
        self.mix(event)