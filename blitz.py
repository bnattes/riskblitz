#!/usr/bin/env python3

import random
import sys

MAX_ATTACK = 3
MAX_DEFEND = 2

attack_start = int(sys.argv[1])
defend_start = int(sys.argv[2])

attack_num = attack_start
defend_num = defend_start

num_rolls = 0

def roll(num):
    return [random.randint(1,6) for i in range(num)]

def battle(attack_roll, defend_roll, attack_num, defend_num):

    for i in range(len(defend_roll)):
        if (len(attack_roll) > 0) and (len(attack_roll) > 0):
            if attack_roll.pop() > defend_roll.pop():
                defend_num -= 1
            else:
                attack_num -= 1

    return (attack_num, defend_num)

while(attack_num > 0 and defend_num > 0):
    if (attack_num >= MAX_ATTACK) and (defend_num >= MAX_DEFEND):
        attack_num, defend_num = battle(roll(MAX_ATTACK), roll(MAX_DEFEND), attack_num, defend_num)

    elif (attack_num >= MAX_ATTACK) and (defend_num < MAX_DEFEND):
        attack_num, defend_num = battle(roll(MAX_ATTACK), roll(defend_num), attack_num, defend_num)

    elif (attack_num < MAX_ATTACK) and (defend_num >= MAX_DEFEND):
        attack_num, defend_num = battle(roll(attack_num), roll(MAX_DEFEND), attack_num, defend_num)

    else:
        attack_num, defend_num = battle(roll(attack_num), roll(defend_num), attack_num, defend_num)
    num_rolls += 1

if attack_num > defend_num:
    print("Attack wins after %d rolls, with %d troop(s) remaining" % (num_rolls, attack_num))
else:
    print("Defend wins after %d rolls, with %d troops remaining" % (num_rolls, defend_num))

print("Casualties:\nAttack: %d\nDefend: %d" % (attack_start-attack_num, defend_start-defend_num))
