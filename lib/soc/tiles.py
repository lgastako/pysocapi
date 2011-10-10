from resources import Resource


class Tile(object):

    @property
    def starting_quantity(self):
        raise NotImplementedError

    def produce(self):
        raise NotImplementedError


class Desert(Tile):
    
    starting_quantity = 1

    def produce(self):
        pass


class SingleResourceTile(Tile):
    """This is the default type of tile in the original game.  Every tile
    produces a single type of resource which is produced with a static
    multiplier of 1 times the number of town/city points each player has on
    adjacent vertices. Subclassing this abstract class is the best way to
    implement a tile with similar behavior. If you want to use a dyanmic
    mulitplier or produce multiple resource types or implement more advanced
    logic for resource production you may be better off extending the Tile
    class directly and implementing your behavior from scratch.    
    """
    
    @property
    def resource(self):
        raise NotImplementedError

    @property
    def produce(self):
        # implement


class Forest(SingleResourceProducingTile):
    resource = Resource.WOOD
    starting_quantity = 4


class Hills(SingleResourceProducingTile):
    resource = Resource.BRICK
    starting_quantity = 3


class Fields(SingleResourceProducingTile):
    resource = Resource.WHEAT
    starting_quantity = 4


class Mountains(SingleResourceProducingTile):
    resource = Resource.ORE
    starting_quantity = 3


class Pasture(SingleResourceProducingTile):
    resource = Resource.SHEEP
    starting_tiles = 4


