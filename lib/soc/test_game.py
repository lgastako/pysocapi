# A game should be able to perform initial layout steps that need to happen
# before the first input from the players is required (specifically that
# of placing the first settlement).  To whit, those steps are:
# 1. Place the tiles randomly.
# 2. Place the numbers on top of the tiles using the human like algorithm
# 3. Place the port overrides
# (Optionally) other expansion set things here.  Code should be written
# with expansion sets in mind from the get go.

import unittest


class TileTypeTest(unittest.TestCase):
    
    def test_default_starting_tiles(self):
        self.assertEquals(1, TileType.DESERT.starting_tile_count)
        self.assertEquals(4, TileType.FOREST.starting_tile_count)
        self.assertEquals(3, TileType.HILLS.starting_tile_count)
        self.assertEquals(4, TileType.FIELDS.starting_tile_count)
        self.assertEquals(3, TileType.MOUNTAINS.starting_tile_count)
        self.assertEquals(4, TileType.PASTURE.starting_tile_count)
        

class TileTest(unittest.TestCase):

    def test_create_default_tile_set(self):
        default_set = Tile.create_default_tile_set()
        for tile in Tile.DEFAULT_TILES:
            count = [x for x in default_set if x == ]
            self.assertEquals

class ResourceTest(unittest.TestCase):
    def test_ALL_is_new_array_each_time(self):
        # We don't want people being able to modify a "singleton" copy
        x = Resource.ALL
        y = Resource.ALL

        # We want them to return an array of the same items each time:
        self.assertEqual(x, y)
        # ...but for the arrays themselves to be different...
        self.assertNotEqual(id(x), id(y))
        # ...so modifications to one...
        x[:] = ["gone", "daddy", "gone"]
        # ...do not affect the other...
        self.assertNotEqual(x, y)
        self.assertTrue(Resource.WOOD in y)


class GameTest(unittest.TestCase):
    
    MINIMUM_SAMPLE_SIZE = 10
    
    def _assert_tile_counts(self, board):
        for resource in Resource.ALL:
            

    def test_initial_layouts_have_proper_tile(self):
        for i in range(self.MINIMUM_SAMPLE_SIZE):
            board = Board.random()
            self._assert_tile_counts(board)
    
    def test_random_board_is_random(self):
        
        