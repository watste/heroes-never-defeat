import pygame as pg

import cons as c
import function as fc
from info import Arms
from info import end_rule


class Map():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.reditime = False  ##是否处于准备状态（即是否显示可攻击域）
        self.history_reditime = False
        self.history_point = []
        self.history_x = 0
        self.history_y = 0
        self.cc = 0
        self.MAP_GRID = c.MAP_GRID
        self.rediman = [0,0]
        self.flag = 0#记录当前行动方
    def createbackground(self):

        for y in range(c.height):
            for x in range(c.width + 1):
                if y % 2 == 1 and x == c.width - 1:
                    continue
                base_x, base_y = fc.getHexMapPos(x, y)
                points = [(base_x, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN, base_y), (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2 + fc.Y_LEN),
                          (base_x + fc.X_LEN, base_y + fc.Y_LEN * 2)]
                pg.draw.lines(self.screen, c.BLACK, True, points)

        pg.draw.line(self.screen, c.BLACK, (0, c.battleheight), (c.MAP_WIDTH, c.battleheight))

    def updatebackground(self):

        pg.draw.polygon(self.screen, c.WHITE,
                        [(0, 0), (0, c.battleheight), (c.MAP_WIDTH, c.battleheight), (c.MAP_WIDTH, 0)])
        pg.draw.line(self.screen, c.BLACK, (0, c.battleheight), (c.MAP_WIDTH, c.battleheight))
        for y in range(c.height):
            for x in range(c.width + 1):
                if y % 2 == 1 and x == c.width - 1:
                    continue
                base_x, base_y = fc.getHexMapPos(x, y)
                points = [(base_x, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN, base_y), (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2 + fc.Y_LEN),
                          (base_x + fc.X_LEN, base_y + fc.Y_LEN * 2)]
                pg.draw.polygon(self.screen, c.WHITE, points)
                pg.draw.lines(self.screen, c.BLACK, True, points)
        x, y = pg.mouse.get_pos()
        x, y = fc.getHexMapIndex(x, y)
        for i in range(c.GRID_X_LEN):
            for j in range(c.GRID_Y_LEN):
                if i == x and j == y:
                    continue
                if self.MAP_GRID[j][i][2] == 1:
                    self.MAP_GRID[j][i][2] = 0

    def cct(self):

        for x in range(c.GRID_X_LEN):
            for y in range(c.GRID_Y_LEN):
                base_x,base_y = fc.getHexMapPos(x,y)
                if self.flag % 2 == 0 and self.MAP_GRID[y][x][2] == 2:
                    points = [(base_x, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x, base_y + fc.Y_LEN // 2),(base_x + fc.X_LEN, base_y), (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2),(base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x + fc.X_LEN, base_y + fc.Y_LEN * 2)]
                    pg.draw.polygon(self.screen, c.GOLD, points)
                    pg.draw.lines(self.screen, (0, 0, 0), True, points)
                elif self.flag % 2 == 1 and self.MAP_GRID[y][x][2] == 3:
                    points = [(base_x, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x, base_y + fc.Y_LEN // 2),
                              (base_x + fc.X_LEN, base_y), (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2),
                              (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2 + fc.Y_LEN),
                              (base_x + fc.X_LEN, base_y + fc.Y_LEN * 2)]
                    pg.draw.polygon(self.screen, c.GOLD, points)
                    pg.draw.lines(self.screen, (0, 0, 0), True, points)


    def createReadiRange(self):
        self.cc += 1
        x, y = pg.mouse.get_pos()
        base_x, base_y = fc.getHexMapIndex(x, y)
        if base_y<9 and ((base_y%2==0 and base_x< 11)or(base_y%2 == 1 and base_x<10)):
        # print(base_x, base_y)
        ##接下来的判断需要实现：不处于reditime 且点击到角色 显示redirange
        #                   处于reditime 且点击到友方  显示友方redirange
        #                   处于reditime 且点击到敌方  判断rediman的攻击模式
        #                                           近战：移动到敌方相邻块 攻击
        #                                           远程；直接攻击
            # 当处于非准备时间，点击角色则会直接进入准备状态
            if ((self.MAP_GRID[base_y][base_x][2] == 2 and self.flag %2 ==0) or (self.MAP_GRID[base_y][base_x][
                2] == 3 and self.flag % 2 == 1)) and self.reditime == False:  # 当处于非准备时间，点击角色则会直接进入准备状态
                # 现在需要判断rediman和当前地图块的关系{如果
                reachrange = Arms.confirm_role(self.MAP_GRID[base_y][base_x][2], self.MAP_GRID[base_y][base_x][1]).speed
                self.rediman = (base_x, base_y)
                for i in range(c.GRID_X_LEN):
                    for j in range(c.GRID_Y_LEN):

                        if fc.calHeuristicDistance(base_x, base_y, i, j) <= reachrange:
                            base_i, base_j = fc.getHexMapPos(i, j)
                            points = [(base_i, base_j + fc.Y_LEN // 2 + fc.Y_LEN), (base_i, base_j + fc.Y_LEN // 2),
                                      (base_i + fc.X_LEN, base_j), (base_i + fc.X_LEN * 2, base_j + fc.Y_LEN // 2),
                                      (base_i + fc.X_LEN * 2, base_j + fc.Y_LEN // 2 + fc.Y_LEN),
                                      (base_i + fc.X_LEN, base_j + fc.Y_LEN * 2)]
                            # if self.MAP_GRID[j][i][] == 1:         判断是否有地形障碍
                            #     continue
                            # else:
                            if self.MAP_GRID[j][i][2] == 0 and (j<9 and ((j%2==0 and i< 11)or(j%2 == 1 and i<10))):
                                pg.draw.polygon(self.screen, (200, 200, 200), points)
                                pg.draw.lines(self.screen, (0, 0, 0), True, points)
                                self.MAP_GRID[j][i][2] = 1
                            elif self.MAP_GRID[j][i][2] == 2:
                                pg.draw.polygon(self.screen, c.SKY_BLUE, points)
                                pg.draw.lines(self.screen, (0, 0, 0), True, points)

                            elif self.MAP_GRID[j][i][2] == 3:
                                pg.draw.polygon(self.screen, c.RED, points)
                                pg.draw.lines(self.screen, (0, 0, 0), True, points)

                # 提供history值
                base_x, base_y = fc.getHexMapPos(base_x, base_y)
                points = [(base_x, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN, base_y), (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2 + fc.Y_LEN),
                          (base_x + fc.X_LEN, base_y + fc.Y_LEN * 2)]
                self.history_point = points
                pg.draw.polygon(self.screen, (200, 200, 200), points)
                pg.draw.lines(self.screen, (0, 0, 0), True, points)
                self.reditime = True
            # 准备状态下点击友军
            elif (self.MAP_GRID[base_y][base_x][2] == self.MAP_GRID[self.rediman[1]][self.rediman[0]][
                2]) and self.reditime == True:#准备状态下点击友军
                reachrange = Arms.confirm_role(self.MAP_GRID[base_y][base_x][2], self.MAP_GRID[base_y][base_x][1]).speed
                self.rediman = (base_x, base_y)
                for i in range(c.GRID_X_LEN):
                    for j in range(c.GRID_Y_LEN):
                        ##绘制攻击范围
                        if fc.calHeuristicDistance(base_x, base_y, i, j) <= reachrange:
                            base_i, base_j = fc.getHexMapPos(i, j)
                            points = [(base_i, base_j + fc.Y_LEN // 2 + fc.Y_LEN), (base_i, base_j + fc.Y_LEN // 2),
                                      (base_i + fc.X_LEN, base_j), (base_i + fc.X_LEN * 2, base_j + fc.Y_LEN // 2),
                                      (base_i + fc.X_LEN * 2, base_j + fc.Y_LEN // 2 + fc.Y_LEN),
                                      (base_i + fc.X_LEN, base_j + fc.Y_LEN * 2)]
                            # if self.MAP_GRID[j][i][] == 1:         判断是否有地形障碍
                            #     continue
                            # else:
                            if self.MAP_GRID[j][i][2] == 0 and (j<9 and ((j%2==0 and i< 11)or(j%2 == 1 and i<10))):
                                pg.draw.polygon(self.screen, (200, 200, 200), points)
                                pg.draw.lines(self.screen, (0, 0, 0), True, points)
                                self.MAP_GRID[j][i][2] = 1
                            elif self.MAP_GRID[j][i][2] == 2:
                                pg.draw.polygon(self.screen, c.SKY_BLUE, points)
                                pg.draw.lines(self.screen, (0, 0, 0), True, points)

                            elif self.MAP_GRID[j][i][2] == 3:
                                pg.draw.polygon(self.screen, c.RED, points)
                                pg.draw.lines(self.screen, (0, 0, 0), True, points)

                # 提供history值
                base_x, base_y = fc.getHexMapPos(base_x, base_y)
                points = [(base_x, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN, base_y), (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2 + fc.Y_LEN),
                          (base_x + fc.X_LEN, base_y + fc.Y_LEN * 2)]
                self.history_point = points
                pg.draw.polygon(self.screen, (200, 200, 200), points)
                pg.draw.lines(self.screen, (0, 0, 0), True, points)
                self.reditime = True
            #在准备状态下点击敌军
            elif ((self.MAP_GRID[base_y][base_x][2] == 2 and self.MAP_GRID[self.rediman[1]][self.rediman[0]][2] == 3) or (
                    self.MAP_GRID[base_y][base_x][2] == 3 and self.MAP_GRID[self.rediman[1]][self.rediman[0]][
                2] == 2)) and self.reditime == True:
                # reachrange = Arms.confirm_role(self.MAP_GRID[base_y][base_x][2], self.MAP_GRID[base_y][base_x][1]).speed
                reachrange = Arms.confirm_role(self.MAP_GRID[self.rediman[1]][self.rediman[0]][2],
                                               self.MAP_GRID[self.rediman[1]][self.rediman[0]][1]).speed
                # 判断攻击模式 如果为近战，进行移动和攻击    如果为远程，则只进行攻击
                if Arms.confirm_role(self.MAP_GRID[self.rediman[1]][self.rediman[0]][2],
                                     self.MAP_GRID[self.rediman[1]][self.rediman[0]][1]).type_of_attack == 0:
                    if fc.calHeuristicDistance(base_x, base_y, self.rediman[0],
                                               self.rediman[1]) <= reachrange + 1:  # 判断攻击距离
                        posx, posy = fc.SearchAttackPos(base_x, base_y, self.rediman[0], self.rediman[1], reachrange,
                                                        self.MAP_GRID)
                        for i in range(4):  ##将地图快的信息转移
                            self.MAP_GRID[posy][posx][i] = self.MAP_GRID[self.rediman[1]][self.rediman[0]][i]
                            print(self.MAP_GRID[posy][posx][i])
                        if posx != self.rediman[0] or posy != self.rediman[1]:
                            for i in range(4):
                                self.MAP_GRID[self.rediman[1]][self.rediman[0]][i] = 0
                        self.reditime = False
                        self.flag+=1 #攻击成功的情况下
                        self.MAP_GRID = Arms.act_attack((posx, posy), (base_x, base_y), self.MAP_GRID)
                else:  # 远程
                    self.reditime = False
                    self.MAP_GRID = Arms.act_attack((self.rediman[0], self.rediman[1]), (base_x, base_y), self.MAP_GRID)
                    self.flag+=1
                self.reditime = False
            elif (self.MAP_GRID[base_y][base_x][2] == 0) and self.reditime == True:
                self.updatebackground()
                self.reditime = False
            elif self.MAP_GRID[base_y][base_x][2] == 1:  ##点击到准备范围之内的地图快时
                for i in range(4):  ##将地图快的信息转移
                    self.MAP_GRID[base_y][base_x][i] = self.MAP_GRID[self.rediman[1]][self.rediman[0]][i]
                for i in range(4):
                    self.MAP_GRID[self.rediman[1]][self.rediman[0]][i] = 0
                self.reditime = False
                self.flag+=1
        pg.draw.line(self.screen, c.BLACK, (0, c.battleheight), (c.MAP_WIDTH, c.battleheight))
    # def UpdateMapGrid(self):

    def currentMouse(self):
        x, y = pg.mouse.get_pos()
        base_x, base_y = fc.getHexMapIndex(x, y)
        if self.reditime == True and base_y < 9:
            if self.cc != 0:  # 在移动后要把之前的标识位置去掉
                ##判断是否为准备区域
                if c.MAP_GRID[self.history_y][self.history_x][2] == 1:
                    pg.draw.polygon(self.screen, (200, 200, 200), self.history_point)
                    pg.draw.lines(self.screen, (0, 0, 0), True, self.history_point)
                elif c.MAP_GRID[self.history_y][self.history_x][2] == 0:
                    pg.draw.polygon(self.screen, (255, 255, 255), self.history_point)
                    pg.draw.lines(self.screen, (0, 0, 0), True, self.history_point)
            if self.MAP_GRID[base_y][base_x][2] == 1:
                self.history_y = base_y
                self.history_x = base_x
                base_x, base_y = fc.getHexMapPos(base_x, base_y)
                points = [(base_x, base_y + fc.Y_LEN // 2 + fc.Y_LEN), (base_x, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN, base_y), (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2),
                          (base_x + fc.X_LEN * 2, base_y + fc.Y_LEN // 2 + fc.Y_LEN),
                          (base_x + fc.X_LEN, base_y + fc.Y_LEN * 2)]
                self.history_point = points

                pg.draw.polygon(self.screen, (200, 200, 0), points)
                pg.draw.lines(self.screen, (0, 0, 0), True, points)

    def map_init(self):
        # m = Map()
        # angel_tower
        self.MAP_GRID[4][2][0] = 0
        self.MAP_GRID[4][2][1] = 1
        self.MAP_GRID[4][2][2] = 2
        self.MAP_GRID[4][2][3] = 1
        # knight_tower
        self.MAP_GRID[5][1][0] = 0
        self.MAP_GRID[5][1][1] = 2
        self.MAP_GRID[5][1][2] = 2
        self.MAP_GRID[5][1][3] = 1
        # wizard_tower
        self.MAP_GRID[3][1][0] = 0
        self.MAP_GRID[3][1][1] = 3
        self.MAP_GRID[3][1][2] = 2
        self.MAP_GRID[3][1][3] = 1
        # griffin_tower
        self.MAP_GRID[6][1][0] = 0
        self.MAP_GRID[6][1][1] = 4
        self.MAP_GRID[6][1][2] = 2
        self.MAP_GRID[6][1][3] = 1
        # swordsman_tower
        self.MAP_GRID[2][1][0] = 0
        self.MAP_GRID[2][1][1] = 5
        self.MAP_GRID[2][1][2] = 2
        self.MAP_GRID[2][1][3] = 1
        # shooter_tower
        self.MAP_GRID[7][0][0] = 0
        self.MAP_GRID[7][0][1] = 6
        self.MAP_GRID[7][0][2] = 2
        self.MAP_GRID[7][0][3] = 1
        # pikeman_tower
        self.MAP_GRID[1][0][0] = 0
        self.MAP_GRID[1][0][1] = 7
        self.MAP_GRID[1][0][2] = 2
        self.MAP_GRID[1][0][3] = 1
        # angel_human
        self.MAP_GRID[4][8][0] = 0
        self.MAP_GRID[4][8][1] = 1
        self.MAP_GRID[4][8][2] = 3
        self.MAP_GRID[4][8][3] = 1
        # knight_human
        self.MAP_GRID[5][8][0] = 0
        self.MAP_GRID[5][8][1] = 2
        self.MAP_GRID[5][8][2] = 3
        self.MAP_GRID[5][8][3] = 1
        # wizard_human
        self.MAP_GRID[3][8][0] = 0
        self.MAP_GRID[3][8][1] = 3
        self.MAP_GRID[3][8][2] = 3
        self.MAP_GRID[3][8][3] = 1
        # griffin_human
        self.MAP_GRID[6][9][0] = 0
        self.MAP_GRID[6][9][1] = 4
        self.MAP_GRID[6][9][2] = 3
        self.MAP_GRID[6][9][3] = 1
        # swordsman_human
        self.MAP_GRID[2][9][0] = 0
        self.MAP_GRID[2][9][1] = 5
        self.MAP_GRID[2][9][2] = 3
        self.MAP_GRID[2][9][3] = 1
        # shooter_human
        self.MAP_GRID[7][9][0] = 0
        self.MAP_GRID[7][9][1] = 6
        self.MAP_GRID[7][9][2] = 3
        self.MAP_GRID[7][9][3] = 1
        # pikeman_human
        self.MAP_GRID[1][9][0] = 0
        self.MAP_GRID[1][9][1] = 7
        self.MAP_GRID[1][9][2] = 3
        self.MAP_GRID[1][9][3] = 1
