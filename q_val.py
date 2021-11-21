import math

from entity import Tiger, Rabbit, Enemy

enemy_list = [Enemy(2 + i, 5) for i in range(4)]

qval = [[0] * 10 for i in range(10)]
for i in range(10):
    for j in range(10):
        if j in range(2, 6) and i == 5:
            qval[i][j] = -3000
        elif j in range(5, 10) and i in range(7, 10):
            qval[i][j] = 12
        elif (j in range(1, 7) and i in (4, 6)) or (j in (1, 6) and i == 5):
            qval[i][j] = -1000
        else:
            qval[i][j] = 0


def heuristic(x, y):
    center = (8, 8)
    return round(12 - math.sqrt(pow(8 - x, 2) + pow(8 - y, 2)), 3)


def tiger_can_attack(tiger, rabbit):
    return math.sqrt(pow(tiger.x - rabbit.x, 2) + pow(tiger.y - rabbit.y, 2)) <= math.sqrt(2)


for i in range(10):
    for j in range(10):
        rabbit_list = [Rabbit(6 + s, 8) for s in range(3)]
        if (j in range(2, 6) and i == 5) or (j in range(6, 9) and i == 8):
            continue
        tiger = Tiger(j, i)
        closed = []
        while rabbit_list:
            tiger_pos = tiger.get_pos()
            closed.append(tiger.get_pos())
            all_near_pos = []
            for k in (-1, 0, 1):
                for m in (-1, 0, 1):
                    if k == m == 0:
                        pass
                    elif 0 <= tiger.y + k <= 9 and 0 <= tiger.x + m <= 9:
                        all_near_pos.append(
                            ((m, k), qval[tiger.y + k][tiger.x + m] + heuristic(tiger.x + m, tiger.y + k))
                        )
            delete_list = []
            for item in all_near_pos:
                qval[tiger.y + item[0][1]][tiger.x + item[0][0]] = item[1]
                if (tiger.x + item[0][0], tiger.y + item[0][1]) in closed:
                    delete_list.append(item)

            for item in delete_list:
                all_near_pos.remove(item)

            all_near_pos.sort(key=lambda x: x[1])
            try:
                tiger.move(*all_near_pos[-1][0])
            except IndexError:
                break

            for rabbit in rabbit_list:
                if tiger_can_attack(tiger, rabbit):
                    qval[tiger.y][tiger.x] += 1000
                    rabbit_list.remove(rabbit)


for str in qval:
    for num in str:
        print(f'{num:.6g}', end=" ")
    print()

from json import dump
dump(qval, open('array.txt', 'w'))
