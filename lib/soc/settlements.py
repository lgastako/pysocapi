class SettlerPile(object):

    def __init__(self, num_resources):
        self.num_resources = num_resources


class Settlement(SettlerPile):

    def __init__(self):
        super(Settlement, self).__init__(1)


class City(SettlerPile):
    
    def __init__(self):
        super(Settlement, self).__init__(2)


