from PIL import Image


MAP_WIDTH = 29
MAP_HEIGHT = 25
TILESIZE = 43

class Tile:

    def __init__(self):
        self.been_seen = 'shadow'

    def see_tile(self):
        self.been_seen = 'seen'

    def get_status(self):
        return self.been_seen



class MapData:

    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.tiles = self.initialize_tiles()


    def initialize_tiles(self):
        tiles = [[Tile() for y in range(self.height)] for x in range(self.width)]
        return tiles


turn_map = MapData(MAP_WIDTH, MAP_HEIGHT)


print('Status of tile 0,0: ' + turn_map.tiles[0][0].get_status())


neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= MAP_WIDTH and
                                   -1 < y <= MAP_HEIGHT and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= MAP_WIDTH) and
                                   (0 <= y2 <= MAP_HEIGHT))]


turn_map.tiles[2][2].been_seen = 'seen'

print('neighbors of 0,0: ' + str(neighbors(0, 0)))

adj_tiles = neighbors(2, 2)

print(str(adj_tiles))

for tile in adj_tiles:
    print(tile)
    turn_map.tiles[tile[0]][tile[1]].been_seen = 'seen'
    

image1 = Image.open('test2.png')
image2 = Image.open('shadow.png')

bg_image = image1.copy()


for y in range(turn_map.height):
    for x in range(turn_map.width):

        if turn_map.tiles[x][y].been_seen == 'shadow':
            bg_image.paste(image2, ((x * TILESIZE), (y * TILESIZE)))



bg_image.save("new_file.png")