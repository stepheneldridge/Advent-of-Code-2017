# A series of tubes
INPUT = open('Day 19.txt', 'r')
data = []
for line in INPUT:
    data.append(list(line[0:-1]))

path = ''
can = True
direction = 2  # 0up 1right 2down 3left
myy = 0
myx = data[myy].index('|')
steps = 1


def find_dir(x, y, dire, data):
    if dire == 0 or dire == 2:
        if x + 1 < len(data[0]) and data[y][x + 1] not in ('+', '|', ' '):
            return 1
        if x - 1 > 0 and data[y][x - 1] not in ('+', '|', ' '):
            return 3
    if dire == 1 or dire == 3:
        if y + 1 < len(data) and data[y + 1][x] not in ('+', '-', ' '):
            return 2
        if y - 1 > 0 and data[y - 1][x] not in ('+', '-', ' '):
            return 0
    return 4


while True:
    if direction == 0:
        myy -= 1
    elif direction == 1:
        myx += 1
    elif direction == 2:
        myy += 1
    elif direction == 3:
        myx -= 1
    else:
        break
    if data[myy][myx] == ' ':
        break
    if data[myy][myx] == '+':
        direction = find_dir(myx, myy, direction, data)
    elif data[myy][myx].isalpha():
        path += data[myy][myx]
    steps += 1
print 'part_1:', path
print 'part_2:', steps
INPUT.close()
