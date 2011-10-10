from collections import OrderedDict


class State(object):

    def __init__(self, game):
        self.game = game
        self.next_state_class = None

    def __call__(self):
        yield 
        return self.next_state_class


class START_STATE(State):
    
    def __init__(self, game):
        super(START_STATE, self).__init__(game)

    def enter(self):
        game.create_board()
        return self.PLACING_INITIAL_SETTLEMENTS


class FIRST_PLAYER_PLACING_FIRST_SETTLEMENT(State):

    def __call__(self):
        game.place_settlement(1, 1)
        yield self.filter_placement(1, 1)


class Game(Emitter):

    def __init__(self, players, tileset, expansions=None):
        self.players = players
        self.tileset = tileset
        self.expansions = expansions

    def start(self):
        # First we notify all of the first class citizens in play of
        # the emitter they should pay attention to.
        for obj in players + tileset + expansions + [self]:
            if hasattr(obj, "set_emitter"):
                obj.set_emitter(self)

        # Then we begin doing the work that generates the initial events
        state = None
        next_state_class = START_STATE
        while True:
            state = next_state_class(self)
            next_state_class = next(state)

    def create_board(self):
        # Place the tiles
        # Place the badges
        # Emit the appropriate events along the way


def main():
    tilese = tileset.TileSet()

    players = OrderedDict([(Color.WHITE, HumanPlayer("John")),
                           (Color.RED, ComputerPlayer("Sun Tzu")),
                           (Color.ORANGE, ComputerPlayer("Alexander")),
                           (Color.BLUE, ComputerPlayer("Shaka"))])

    game = Game(players,
                tileset,
                expansions)

    game.start()
