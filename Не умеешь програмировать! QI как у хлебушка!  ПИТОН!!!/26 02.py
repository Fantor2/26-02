import pygame as pg
import sys
from grass import Grass
from settings import *
FPS=60
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

pg.init()
screen= pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pg.time.Clock()
grass = Grass("grass.png",screen , x, y)
while True:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

grass.update()
screen_fill((0,0,0))
pg.display.update()
