from PIL import Image
import numpy

MAP_WIDTH = 10
MAP_HEIGHT = 10
TILESIZE = 44


mapdata = [["G" for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

mapdata[0][0]  = "M"
mapdata[0][1]  = "M"
mapdata[0][2]  = "M"
mapdata[0][3]  = "M"

print(mapdata)

canvas = Image.new("RGB", (MAP_WIDTH * TILESIZE, MAP_HEIGHT * TILESIZE))
mountainImage = Image.open("mountains.png")
grassImage = Image.open("grass.png")


for x in range(MAP_WIDTH):
    for y in range(MAP_HEIGHT):
        if mapdata[x][y] == "M":
            canvas.paste(mountainImage, ((x * TILESIZE), (y * TILESIZE)))
        else:
            canvas.paste(grassImage, ((x * TILESIZE), (y * TILESIZE)))

canvas.show()
