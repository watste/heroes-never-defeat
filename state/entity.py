import cons as c
import function as fc


class entity():
    def __init__(self):
        self.a = 0

    def loadImage(self, screen, MAP_GRID, GFX):
        for x in range(c.GRID_X_LEN):
            for y in range(c.GRID_Y_LEN):
                if MAP_GRID[y][x][2] == 2:
                    if MAP_GRID[y][x][1] == 1:
                        screen.blit(GFX['angel_tower'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 2:
                        screen.blit(GFX['knight_tower'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 3:
                        screen.blit(GFX['wizard_tower'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 4:
                        screen.blit(GFX['griffin_tower'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 5:
                        screen.blit(GFX['swordsman_tower'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 6:
                        screen.blit(GFX['shooter_tower'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    else:
                        screen.blit(GFX['pikeman_tower'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                elif MAP_GRID[y][x][2] == 3 :
                    if MAP_GRID[y][x][1] == 1:
                        screen.blit(GFX['angel_human'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 2:
                        screen.blit(GFX['knight_human'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 3:
                        screen.blit(GFX['wizard_human'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 4:
                        screen.blit(GFX['griffin_human'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 5:
                        screen.blit(GFX['swordsman_human'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    elif MAP_GRID[y][x][1] == 6:
                        screen.blit(GFX['shooter_human'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])
                    else:
                        screen.blit(GFX['pikeman_human'], fc.IndexGetMapPos(x, y), c.ImageDistri['front_1'])

