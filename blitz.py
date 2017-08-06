import random
import sys

attack_num = int(sys.argv[1])
defend_num = int(sys.argv[2])

def roll(num):
    dice = []

    for i in range(0,num):
        dice.append(random.randint(1,6))
        dice = sorted(dice)

    return dice

a = roll(attack_num)
d = roll(defend_num)
print(a)
print(d)
