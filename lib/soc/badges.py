class Badge(object):
    def __init__(self, number):
        # Dots should be deriveable - but is based on # of dice. 
        # Expansion could change?
        # Should we include letters to do authentic setup/display?
        self.number = number

class BadgeSet(set):
    