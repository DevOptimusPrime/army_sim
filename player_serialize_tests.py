import dataclasses
from faction_engine import SimpleFaction
import json

MAP_WIDTH = 10
MAP_HEIGHT = 10
TILESIZE = 44

player_map_knowledge = [["N" for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

player_map_knowledge[0][0] = "Y"
player_map_knowledge[0][1] = "Y"
player_map_knowledge[1][0] = "Y"
player_map_knowledge[1][1] = "Y"
player_map_knowledge[1][2] = "Y"
player_map_knowledge[1][3] = "Y"

romans = SimpleFaction("Romans", 3, 2, 3, 6, player_map_knowledge, [1,1], [0,0])


with open('romans.json', 'w') as outfile:
    json.dump(dataclasses.asdict(romans), outfile)

