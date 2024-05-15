# 判胜规则
#   1.对方所有兵种被消灭
#   2.对方中途离开游戏
#   3.对方走棋事件用完
# 和棋规则
#   在连续100回合内不分胜负
import time
from info import battlepath
# import Arms


def end_judge():
    if battlepath.online_tower == 0:
        battlepath.end_of_flag = 1
    elif battlepath.online_human == 0:
        battlepath.end_of_flag = -1

    if battlepath.surplus_round == 0 and battlepath.end_of_flag != 2:
        battlepath.end_of_flag = 0
    else:
        if battlepath.tower_nom == 0:
            battlepath.end_of_flag = 1
        elif battlepath.human_nom == 0:
            battlepath.end_of_flag = -1

    if battlepath.surplus_round == 0:
        battlepath.end_of_flag = 0


def output_end():
    print(time.strftime("[%H:%M:%S]", time.localtime()), end="")
    if battlepath.end_of_flag == -1:
        if battlepath.online_human == 0:
            print("人类阵营离开战斗，城堡阵营获胜！")
        else:
            print("人类阵营被消灭，城堡阵营获胜！")
    elif battlepath.end_of_flag == 0:
        print("平局")
    elif battlepath.end_of_flag == 1:
        if battlepath.online_tower == 0:
            print("城堡阵营离开战斗，人类阵营获胜！")
        else:
            print("城堡阵营被消灭，人类阵营获胜！")
    battlepath.ended_flag = 1


# 示例
#
# while battlepath.py.end_of_flag == 2:
#     print("剩余回合数:", battlepath.py.surplus_round)
#
#     # 每次用户操作结束后进行游戏结果判定
#     if Arms.angel_tower.num != 0 and Arms.knight_human.num != 0:
#         Arms.angel_tower.get_damage(Arms.knight_human)
#     print("城堡阵营剩余数量:", battlepath.py.tower_nom)
#     end_judge()
#     if battlepath.py.end_of_flag != 2:
#         output_end()
#         break
#
#     if Arms.knight_human.num != 0 and Arms.angel_tower.num != 0:
#         Arms.knight_human.get_damage(Arms.angel_tower)
#     print("人类阵营剩余数量:", battlepath.py.human_nom)
#     end_judge()
#     if battlepath.py.end_of_flag != 2:
#         output_end()
#         break
#
#     if battlepath.py.tower_nom == 6:
#         battlepath.py.online_human = 0
#     end_judge()
#     if battlepath.py.end_of_flag != 2:
#         output_end()
#         break
#
#     battlepath.py.surplus_round -= 1
