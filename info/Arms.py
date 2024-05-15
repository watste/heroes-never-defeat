import time
from info import battlepath


class Arms:
    def __init__(self, type_arms, camp):
        if type_arms == 1:
            self.name = "天使"  # 兵种名称
            self.num = 1  # 兵种数量
            self.hp = 200  # 兵种血量
            self.speed = 10  # 可移动格数
            self.atk = 20  # 兵种攻击力
            self.camp = camp  # 所属阵营 2=城堡 3=人类
            self.type_of_attack = 0  # 攻击方式 0=近战 1=远程

        elif type_arms == 2:
            self.name = "骑士"  # 兵种名称
            self.num = 2  # 兵种数量
            self.hp = 100  # 兵种血量
            self.speed = 6  # 可移动格数
            self.atk = 15  # 兵种攻击力
            self.camp = camp  # 所属阵营 2=城堡 3=人类
            self.type_of_attack = 0  # 攻击方式 0=近战 1=远程

        elif type_arms == 3:
            self.name = "法师"  # 兵种名称
            self.num = 3  # 兵种数量
            self.hp = 40  # 兵种血量
            self.speed = 5  # 可移动格数
            self.atk = 12  # 兵种攻击力
            self.camp = camp  # 所属阵营 2=城堡 3=人类
            self.type_of_attack = 1  # 攻击方式 0=近战 1=远程

        elif type_arms == 6:
            self.name = "射手"  # 兵种名称
            self.num = 9  # 兵种数量
            self.hp = 12  # 兵种血量
            self.speed = 2  # 可移动格数
            self.atk = 60  # 兵种攻击力
            self.camp = camp  # 所属阵营 2=城堡 3=人类
            self.type_of_attack = 1  # 攻击方式 0=近战 1=远程

        elif type_arms == 4:
            self.name = "狮鹫"  # 兵种名称
            self.num = 7  # 兵种数量
            self.hp = 25  # 兵种血量
            self.speed = 5  # 可移动格数
            self.atk = 8  # 兵种攻击力
            self.camp = camp  # 所属阵营 2=城堡 3=人类
            self.type_of_attack = 0  # 攻击方式 0=近战 1=远程

        elif type_arms == 5:
            self.name = "剑士"  # 兵种名称
            self.num = 4  # 兵种数量
            self.hp = 35  # 兵种血量
            self.speed = 3  # 可移动格数
            self.atk = 10  # 兵种攻击力
            self.camp = camp  # 所属阵营 2=城堡 3=人类
            self.type_of_attack = 0  # 攻击方式 0=近战 1=远程

        elif type_arms == 7:
            self.name = "枪兵"  # 兵种名称
            self.num = 14  # 兵种数量
            self.hp = 10  # 兵种血量
            self.speed = 1  # 可移动格数
            self.atk = 4  # 兵种攻击力
            self.camp = camp  # 所属阵营 2=城堡 3=人类
            self.type_of_attack = 0  # 攻击方式 0=近战 1=远程

        self.hp_total = self.hp * self.num

    def info(self):
        print("新创建角色:", self.name)
        print("数量:", self.num)
        print("单个兵种血量:", self.hp)
        print("总血量", self.hp_total)
        print("移速:", self.speed)
        print("攻击力:", self.atk)
        if self.camp == 0:
            print("所属势力: 城堡")
        else:
            print("所属势力: 人类")
        if self.type_of_attack == 0:
            print("攻击方式: 近战")
        else:
            print("攻击方式: 远程")

    def damage(self):
        return self.num * self.atk

    def get_damage(self, attacker):
        num_pre = self.num
        self.hp_total -= attacker.damage()
        print(time.strftime("[%H:%M:%S]", time.localtime()), end="")
        if self.hp_total % self.hp == 0:
            self.num = self.hp_total // self.hp
        else:
            self.num = self.hp_total // self.hp + 1
        if self.camp == 2:
            print("城堡阵营的", self.name, sep="", end="")
        else:
            print("人类阵营的", self.name, sep="", end="")
        if self.hp_total <= 0:
            self.hp_total = 0
            self.num = 0
            print("受到来自敌方", attacker.name, "的", attacker.damage(), "点伤害,造成", num_pre - self.num,
                  "个死亡，存活", self.num,
                  "个,", sep="", end="")
            print("该", self.name, "单位阵亡!", sep="")
        else:
            print("受到来自敌方", attacker.name, "的", attacker.damage(), "点伤害,造成", num_pre - self.num,
                  "个死亡，存活", self.num,
                  "个",
                  sep="")
        if self.num == 0:
            if self.camp == 2:
                battlepath.tower_nom -= 1
            else:
                battlepath.human_nom -= 1


def confirm_role(camp, arms):
    if camp == 2:
        if arms == 1:
            return angel_tower
        elif arms == 2:
            return knight_tower
        elif arms == 3:
            return wizard_tower
        elif arms == 4:
            return griffin_tower
        elif arms == 5:
            return swordsman_tower
        elif arms == 6:
            return shooter_tower
        elif arms == 7:
            return pikeman_tower
    else:
        if arms == 1:
            return angel_human
        elif arms == 2:
            return knight_human
        elif arms == 3:
            return wizard_human
        elif arms == 4:
            return griffin_human
        elif arms == 5:
            return swordsman_human
        elif arms == 6:
            return shooter_human
        elif arms == 7:
            return pikeman_human


def act_attack(attacker, attacked, map_grid):
    A = confirm_role(map_grid[attacked[1]][attacked[0]][2], map_grid[attacked[1]][attacked[0]][1])
    B = confirm_role(map_grid[attacker[1]][attacker[0]][2], map_grid[attacker[1]][attacker[0]][1])
    A.get_damage(B)
    if dead_judge(A):
        for i in range(4):
            map_grid[attacked[1]][attacked[0]][i] = 0
    return map_grid

def dead_judge(arms):
    if arms.num == 0:
        return True
    else:
        return False


angel_tower = Arms(1, 2)
knight_tower = Arms(2, 2)
wizard_tower = Arms(3, 2)
griffin_tower = Arms(4, 2)
swordsman_tower = Arms(5, 2)
shooter_tower = Arms(6, 2)
pikeman_tower = Arms(7, 2)
angel_human = Arms(1, 3)
knight_human = Arms(2, 3)
wizard_human = Arms(3, 3)
griffin_human = Arms(4, 3)
swordsman_human = Arms(5, 3)
shooter_human = Arms(6, 3)
pikeman_human = Arms(7, 3)
