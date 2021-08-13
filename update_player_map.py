import json
from faction_engine import SimpleFaction, LoadPlayer
from dataclasses import dataclass
from PIL import Image


MAP_WIDTH = 10
MAP_HEIGHT = 10
TILESIZE = 44

worldmap = [["G" for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

romans = LoadPlayer('romans.json')


# TODO: need to take player and movement orders to update location and mapknowledge with neighbors of seen squares
def update_player_map_knowledge(player: SimpleFaction) -> SimpleFaction:
    pass

# TODO: Need to update to take player class and the world map data class to compare and draw icons
def update_player_map_view(player: SimpleFaction) -> Image:
    canvas = Image.new("RGB", (MAP_WIDTH * TILESIZE, MAP_HEIGHT * TILESIZE))
    mountainImage = Image.open("mountains.png")
    grassImage = Image.open("grass.png")
    fowImage = Image.open("FOW.png")

    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            if player.MapKnowledge[x][y] == "N":
                canvas.paste(fowImage, ((x * TILESIZE), (y * TILESIZE)))
            else:
                canvas.paste(grassImage, ((x * TILESIZE), (y * TILESIZE)))

    return canvas

mapImage = update_player_map_view(romans)

mapImage.show()

