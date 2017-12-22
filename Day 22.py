# Sporifica Virus
INPUT = open('Day 22.txt', 'r')
grid = {}
i = 0
for line in INPUT:
    grid[i] = {}
    for a in xrange(len(line)):
        if line[a] == '\n':
            continue
        grid[i][a] = line[a]
    i += 1

def get(x, y, grid):
    if x in grid:
        if y in grid[x]:
            return grid[x][y]
        else:
            grid[x][y] = '.'
            return grid[x][y]
    else:
        grid[x] = {}
        grid[x][y] = '.'
        return grid[x][y]


def part_1():
    direction = 0 # up right down left
    cur = [12, 12]
    turned = 0
    for a in xrange(10000):
        node = get(cur[0], cur[1], grid)
        if node == '#':
            direction += 1
        elif node == '.':
            direction -= 1
        direction %= 4
        if node == '#':
            grid[cur[0]][cur[1]] = '.'
        elif node == '.':
            grid[cur[0]][cur[1]] = '#'
            turned += 1
        if direction == 0:
            cur[0] -= 1
        elif direction == 1:
            cur[1] += 1
        elif direction == 2:
            cur[0] += 1
        elif direction == 3:
            cur[1] -= 1
    print 'part_1:', turned
INPUT.close()
part_1()
INPUT = open('Day 22.txt', 'r')
grid = {}
i = 0
for line in INPUT:
    grid[i] = {}
    for a in xrange(len(line)):
        if line[a] == '\n':
            continue
        grid[i][a] = line[a]
    i += 1


def part_2():
    direction = 0 # up right down left
    cur = [12, 12]
    turned = 0
    for a in xrange(10000000):
        node = get(cur[0], cur[1], grid)
        if node == '#':
            direction += 1
        elif node == '.':
            direction -= 1
        elif node == 'F':
            direction += 2
        direction %= 4
        if node == '#':
            grid[cur[0]][cur[1]] = 'F'
        elif node == 'F':
            grid[cur[0]][cur[1]] = '.'
        elif node == 'W':
            grid[cur[0]][cur[1]] = '#'
            turned += 1
        else:
            grid[cur[0]][cur[1]] = 'W'
        if direction == 0:
            cur[0] -= 1
        elif direction == 1:
            cur[1] += 1
        elif direction == 2:
            cur[0] += 1
        elif direction == 3:
            cur[1] -= 1
    print 'part_2:', turned
INPUT.close()
part_2()
