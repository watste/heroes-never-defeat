import Arms


def confirm_role(camp, arms):
    if camp == 0:
        if arms == 1:
            return Arms.angel_tower
        elif arms == 2:
            return Arms.knight_tower
        elif arms == 3:
            return Arms.wizard_tower
        elif arms == 4:
            return Arms.griffin_tower
        elif arms == 5:
            return Arms.swordsman_tower
        elif arms == 6:
            return Arms.shooter_tower
        elif arms == 7:
            return Arms.pikeman_tower
    else:
        if arms == 1:
            return Arms.angel_human
        elif arms == 2:
            return Arms.knight_human
        elif arms == 3:
            return Arms.wizard_human
        elif arms == 4:
            return Arms.griffin_human
        elif arms == 5:
            return Arms.swordsman_human
        elif arms == 6:
            return Arms.shooter_human
        elif arms == 7:
            return Arms.pikeman_human


def move_arms(x_init, y_init, x_target, y_target, camp, arms, status, block):
    # 进行移动
    """
    for i in range(0, confirm_role((camp, arms)).speed):
        if x_init < x_target and MAP_GRID.block == 0:
            x_init += 1
        elif x_init > x_target:
            x_init -= 1
        if y_init < y_target:
            y_init += 1
        elif y_init > y_target:
            y_init -= 1
        if x_init == x_target and y_init == y_target:
            break"""


def act_attack(attacker, attacked):
    attacked.get_damage(attacker)


def act_selected(selected, site):
    if selected.type_of_attack == 1:
        if site[3] == 0:
            move_arms(site)
        else:
            act_attack(selected, confirm_role(site[1], site[2]))
    else:
        move_arms(site)
        act_attack(selected, confirm_role(site[1], site[2]))


arm = confirm_role(0, 1)
act_attack(Arms.pikeman_human, confirm_role(0, 1))
confirm_role(0, 1).info()
