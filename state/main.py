import os

import pygame as pg

import cons as c
import entity
import function as fc
import map
from info import end_rule
from info import battlepath as p

###初始化###
pg.init()

screen = pg.display.set_mode((c.MAP_WIDTH, c.MAP_HEIGHT), 0, 32)
pg.display.set_caption("heroes")
screen.fill((255, 255, 255))
# 以下部分是地图设计
e = entity.entity()
m = map.Map()
m.map_init()
print(fc.calHeuristicDistance(4, 4, 5, 2))
m.createbackground()
pg.display.flip()
GFX = fc.load_all_gfx(os.path.join(r'..\resources\graphics'))
e.loadImage(screen, m.MAP_GRID, GFX)
######自此以上是地图的背景部分，包括网格等#####
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:  ##在按下鼠标之后，当前块和攻击范围内的块亮起
            m.updatebackground()
            m.cct()
            m.createReadiRange()
            e.loadImage(screen, m.MAP_GRID, GFX)

            pg.display.update()
            end_rule.end_judge()
            if p.ended_flag == 0 and p.end_of_flag != 2:
                end_rule.output_end()
        if event.type == pg.MOUSEMOTION:
            m.currentMouse()
            e.loadImage(screen, m.MAP_GRID, GFX)
            pg.display.update()
