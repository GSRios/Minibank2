class Mix(object):
    def __init__(self, events=None):
        if events is not None:
            for event in events:
                self.mix(event)


    def mix(self, event):
        method_name = '{}'.format(event.__class__.__name__.lower())
        method = getattr(self, method_name)
        method(event)