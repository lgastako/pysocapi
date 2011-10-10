import tiles

class TileSet(set):
    
    TILE_CLASSES = [tiles.DESERT,
                    tiles.WOOD,
                    tiles.BRICK,
                    tiles.WHEAT,
                    tiles.ORE,
                    tiles.SHEEP]

    def __init__(self):
        super(TileSet, set).__init__(
            [[tile] * tile.starting_tiles
            for tile in cls.TILE_CLASSES])
