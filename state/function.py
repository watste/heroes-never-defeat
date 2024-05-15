import cons as c
import os
import pygame as pg
X_LEN = c.HEX_X_SIZE // 2
Y_LEN = c.HEX_Y_SIZE // 2
def getHexMapPos(x, y):  # 获得当前六边形的左上端点
    if y % 2 == 0:
        base_x = X_LEN * 2 * x
        base_y = Y_LEN * 3 * (y // 2)
    else:
        base_x = X_LEN * 2 * x + X_LEN
        base_y = Y_LEN * 3 * (y // 2) + Y_LEN // 2 + Y_LEN
    return (base_x, base_y)##
class Vector2d():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def minus(self, vec):
        return Vector2d(self.x - vec.x, self.y - vec.y)

    def crossProduct(self, vec):
        return (self.x * vec.y - self.y * vec.x)

def isInTriangle(x1, y1, x2, y2, x3, y3, x, y):
    A = Vector2d(x1, y1)
    B = Vector2d(x2, y2)
    C = Vector2d(x3, y3)
    P = Vector2d(x, y)
    PA = A.minus(P)
    PB = B.minus(P)
    PC = C.minus(P)
    t1 = PA.crossProduct(PB)
    t2 = PB.crossProduct(PC)
    t3 = PC.crossProduct(PA)
    if (t1 * t2 >= 0) and (t1 * t3 >= 0):
        return True
    return False
def getHexMapIndex(x, y):
    X_LEN = c.HEX_X_SIZE // 2
    Y_LEN = c.HEX_Y_SIZE // 2
    tmp_x, offset_x = divmod(x, c.HEX_X_SIZE)
    tmp_y, offset_y = divmod(y, Y_LEN * 3)
    map_x, map_y = 0, 0
    if offset_y <= (Y_LEN + Y_LEN//2):
        if offset_y >= Y_LEN//2:
            map_x, map_y = tmp_x, tmp_y * 2
        else:
            triangle_list = [(0, 0, 0, Y_LEN//2, X_LEN, 0),
                             (0, Y_LEN//2, X_LEN, 0, c.HEX_X_SIZE, Y_LEN//2),
                             (X_LEN, 0, c.HEX_X_SIZE, 0, c.HEX_X_SIZE, Y_LEN//2)]
            map_list = [(tmp_x - 1, tmp_y * 2 -1), (tmp_x, tmp_y * 2), (tmp_x, tmp_y * 2 -1)]
            for i, data in enumerate(triangle_list):
                if isInTriangle(*data, offset_x, offset_y):
                    map_x, map_y = map_list[i]
                    break
    elif offset_y >= c.HEX_Y_SIZE:
        if offset_x <= X_LEN:
            map_x, map_y = tmp_x - 1, tmp_y * 2 + 1
        else:
            map_x, map_y = tmp_x, tmp_y *2 + 1
    else:
        triangle_list = [(0, Y_LEN + Y_LEN//2, 0, c.HEX_Y_SIZE, X_LEN, c.HEX_Y_SIZE),
                         (0, Y_LEN + Y_LEN//2, X_LEN, c.HEX_Y_SIZE, c.HEX_X_SIZE, Y_LEN + Y_LEN//2),
                         (X_LEN, c.HEX_Y_SIZE, c.HEX_X_SIZE, Y_LEN + Y_LEN//2, c.HEX_X_SIZE, c.HEX_Y_SIZE)]
        map_list = [(tmp_x - 1, tmp_y * 2 + 1), (tmp_x, tmp_y * 2), (tmp_x, tmp_y *2 + 1)]
        for i, data in enumerate(triangle_list):
            if isInTriangle(*data, offset_x, offset_y):
                map_x, map_y = map_list[i]
                break
    if map_x == 0 and map_y == 0:
        print('pos[%d, %d](%d, %d) base[%d, %d] off[%d, %d] ' % (map_x, map_y, x, y, tmp_x, tmp_y, offset_x, offset_y))
    return (map_x, map_y)
def calHeuristicDistance(x1, y1, x2, y2):#利用立方体坐标计算距离
   x1 = x1-y1//2
   x2 = x2-y2//2
   z1 = -x1-y1
   z2 = -x2-y2
   distance = (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))//2
   return distance

def IndexGetMapPos(x,y):
    pos_x = 0
    pos_y = 0
    if y%2==0:
        pos_x = x*c.HEX_X_SIZE+c.HEX_X_SIZE*0.25
    else: pos_x = x*c.HEX_X_SIZE+c.HEX_X_SIZE//1.5
    if y==0:
        pos_y = 0
    else:
        pos_y = y*c.HEX_Y_SIZE*2//3+c.HEX_Y_SIZE//2

    return pos_x,pos_y

# def loadFrames(sheet):
#     frame_rect_list = [(64, 0, 32, 32), (96, 0, 32, 32)]
#     for frame_rect in frame_rect_list:
#         self.frames.append(get_image(sheet, *frame_rect,
#                                           c.BLACK, c.SIZE_MULTIPLIER))
def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pg.Surface([width, height])
    rect = image.get_rect()

    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pg.transform.scale(image,
                               (int(rect.width * scale),
                                int(rect.height * scale)))
    return image
def load_all_gfx(directory, colorkey=c.WHITE, accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics

def SearchAttackPos(x,y,redix,rediy,reachrange,map_grid):#寻找战斗时需要到达的位置
    if calHeuristicDistance(redix, rediy, x, y)<=1:
        print(11)
        print(redix,rediy)
        return redix,rediy
    redirange = []
    cnt = 0
    for i in range(c.GRID_X_LEN):
        for j in range(c.GRID_Y_LEN):
            if calHeuristicDistance(redix, rediy, i, j)<=reachrange and calHeuristicDistance(x, y, i, j)==1 and map_grid[j][i][3]==0:
                print(i,j)
                print(calHeuristicDistance(redix, rediy, i, j))
                print(calHeuristicDistance(x, y, i, j))
                cnt+=1
                redirange.append((i,j))
    min = redirange[0]
    for i in range(cnt):
        if calHeuristicDistance(redix, rediy, redirange[i][0], redirange[i][1]) < calHeuristicDistance(redix, rediy, min[0], min[1]):
            min = redirange[i]
    return min[0],min[1]