# Spiral memory
# 501, 501 grid
import math
INPUT = 368078
DATA = []
SIZE = 13


def add_around(data, point):
    x, y = point
    return data[x + 1][y] + data[x][y + 1] + data[x + 1][y + 1] + data[x - 1][y + 1] + data[x + 1][y - 1] + data[x - 1][y] + data[x][y - 1] + data[x - 1][y - 1]


def populate():
    for i in xrange(SIZE):
        row = []
        for j in xrange(SIZE):
            row.append(0)
        DATA.append(row)


def func():
    length = 1
    direction = 0  # R U L D
    point = [SIZE / 2, SIZE / 2]
    DATA[SIZE / 2][SIZE / 2] = 1
    for i in xrange(SIZE * SIZE):
        length = int(math.floor(i / 2) + 1)
        for j in xrange(length):
            if direction == 0:
                point[0] = point[0] + 1
            elif direction == 1:
                point[1] = point[1] + 1
            elif direction == 2:
                point[0] = point[0] - 1
            elif direction == 3:
                point[1] = point[1] - 1
            if add_around(DATA, point) > INPUT:
                print add_around(DATA, point)
                return
            DATA[point[0]][point[1]] = add_around(DATA, point)
        direction = (direction + 1) % 4


def part_1():
    size = math.ceil(math.sqrt(INPUT))
    if size % 2 == 0:
        size = size + 1
    print int(math.floor(size / 2) + abs(((size - 1) / 2) - ((size * size - INPUT) % (size - 1))))


def part_2():
    populate()
    func()


part_1()
part_2()
