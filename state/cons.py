MAP_HEXAGON = False
ORIGINAL_CAPTION = 'RPG Game'
GRID_X_LEN = 11
GRID_Y_LEN = 9
mutate = 1.5#地图放大倍数
battleheight = 620
height = 9
width =11
REC_SIZE = 56
HEX_Y_SIZE = 88
HEX_X_SIZE = 76
MAP_WIDTH = (GRID_X_LEN * HEX_X_SIZE)*mutate-420
MAP_HEIGHT = 450*mutate

# if MAP_HEXAGON:
#     REC_SIZE = 56
#     HEX_Y_SIZE = 56
#     HEX_X_SIZE = 48
#     MAP_WIDTH = GRID_X_LEN * HEX_X_SIZE + HEX_X_SIZE//4
#     MAP_HEIGHT = GRID_Y_LEN//2 * (HEX_Y_SIZE//2) * 3 + HEX_Y_SIZE//4
# else:
#     REC_SIZE = 50
#     MAP_WIDTH = GRID_X_LEN * REC_SIZE
#     MAP_HEIGHT = GRID_Y_LEN * REC_SIZE
MAP_GRID = [[[0 for _ in range(4)] for _ in range(11)]for _ in range(9)]
    #第一个参数没用                                        #四个参数分别为：阵营，兵种，状态，障碍
                                            #兵种为0表示为空格
                                            #状态： 0--空格   1--可行域   2--A方占有   3--B方占有
                                            #0为无障碍，1为有障碍



WHITE        = (255, 255, 255)
NAVYBLUE     = ( 60,  60, 100)
SKY_BLUE     = ( 39, 145, 251)
BLACK        = (  0,   0,   0)
LIGHTYELLOW  = (247, 238, 214)
RED          = (255,   0,   0)
PURPLE       = (255,   0, 255)
GOLD         = (255, 215,   0)
GREEN        = (  0, 255,   0)

SIZE_MULTIPLIER = 1.3

#GAME INFO DICTIONARY KEYS
CURRENT_TIME = 'current time'
LEVEL_NUM = 'level num'

#STATES FOR ENTIRE GAME
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
GAME_OVER = 'game over'
LEVEL = 'level'

#MAP BACKGROUND STATE
BG_EMPTY = 0
BG_ACTIVE = 1
BG_RANGE = 2
BG_SELECT = 3
BG_ATTACK = 4

#MAP GRID TYPE
MAP_EMPTY = 0
MAP_STONE = 1
MAP_GRASS = 2
MAP_DESERT = 3
MAP_LAKE = 4

GROUP1 = 'group1'
GROUP2 = 'group2'
# MAP_GRID = 'mapgrid'

#Entity State
IDLE = 'idle'
WALK = 'walk'
ATTACK = 'attack'

#Entity Attribute
ATTR_HEALTH = 'health'
ATTR_RANGE = 'range'
ATTR_DAMAGE = 'damage'
ATTR_ATTACK = 'attack'
ATTR_DEFENSE = 'defense'
ATTR_REMOTE = 'remote' # remote army or melee army
ATTR_SPEED = 'speed' # higher speed army can act prior to lower speed army in a game turn

#Entity Name
DEVIL = 'devil'
SOLDIER = 'footman'
MAGICIAN = 'magician'
FIREBALL = 'fireball'
MOUSE = 'mouse'

#Game State
INIT = 'init'
SELECT = 'select'
ENTITY_ACT = 'entity act'

#Game Setting
MOVE_SPEED = 2

#图片切分
ImageDistri ={'front_1':(5,0,60,60),
 'front_2':(96,0,32,32),
 'back_1':(0,0,32,32),
 'back_2':(32,0,32,32),
 'left_1':(0,32,32,64),
 'left_2':(32,32,64,64),
 'right_1':(64,32,96,64),
 'right_2':(96,32,128,64)
}
