from entity import Tiger, Rabbit, Enemy
from  q_val import tiger_can_attack
from json import load
import random

map = load(open('array.txt', 'r'))

enemy_list = [Enemy(2 + i, 5) for i in range(4)]
rabbit_list = [Rabbit(6 + s, 8) for s in range(3)]

x = random.randint(0, 10)
y = random.randint(0, 10)

while x in range(2, 6) and y == 5:
    x = random.randint(0, 10)
    y = random.randint(0, 10)

tiger = Tiger(x, y)


def draw():
    for i in range(10):
        for j in range(10):
            flag = True
            for rabit in rabbit_list:
                if (j, i) == rabit.get_pos():
                    print('r', end='')
                    flag = False
            for enemy in enemy_list:
                if (j, i) == enemy.get_pos():
                    print('e', end='')
                    flag = False
            if (j, i) == tiger.get_pos():
                print('t', end='')
                flag = False
            if flag:
                print('.', end='')
        print()
    print("--------")


while rabbit_list:
    all_near_pos = []

    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j == 0:
                pass
            elif 0 <= tiger.y + i <= 9 and 0 <= tiger.x + j <= 9:
                all_near_pos.append(
                    ((j, i), map[tiger.y + i][tiger.x + j])
                )

    all_near_pos.sort(key=lambda x: x[1])

    tiger.move(*all_near_pos[-1][0])

    for rabbit in rabbit_list:
        if tiger_can_attack(tiger, rabbit):
            rabbit_list.remove(rabbit)
    draw()
