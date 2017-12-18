# Duet
import re
INPUT = open('Day 18.txt', 'r')
commands = []
reg = {}
reg0 = {}
reg1 = {}
for line in INPUT:
    stuff = re.split('\s+', line)
    try:
        stuff[1] = int(stuff[1])
    except Exception:
        reg[stuff[1]] = 0
        reg0[stuff[1]] = 0
        reg1[stuff[1]] = 1
    try:
        stuff[2] = int(stuff[2])
    except Exception:
        reg[stuff[2]] = 0
        reg0[stuff[2]] = 0
        reg1[stuff[2]] = 1
    commands.append(stuff)

index = 0
last = -1000000000
while True:
    c = commands[index]
    if c[0] == 'set':
        reg[c[1]] = c[2] if isinstance(c[2], int) else reg[c[2]]
    elif c[0] == 'mul':
        reg[c[1]] *= c[2] if isinstance(c[2], int) else reg[c[2]]
    elif c[0] == 'add':
        reg[c[1]] += c[2] if isinstance(c[2], int) else reg[c[2]]
    elif c[0] == 'mod':
        a = c[2] if isinstance(c[2], int) else reg[c[2]]
        reg[c[1]] %= a
    elif c[0] == 'rcv':
        if (c[1] if isinstance(c[1], int) else reg[c[1]]) != 0:
            print 'part_1:', last
            break
    elif c[0] == 'snd':
        last = (c[1] if isinstance(c[1], int) else reg[c[1]])
    if c[0] == 'jgz':
        index += (c[2] if isinstance(c[2], int) else reg[c[2]]) if (c[1] if isinstance(c[1], int) else reg[c[1]]) > 0 else 1
    else:
        index += 1
    if index < 0 or index >= len(commands):
        break


def part_2():
    send0 = []
    send1 = []
    current = 0
    r1 = True
    r2 = True
    index = [0, 0, 0]

    def runone(reg, index, snd, id):
        c = commands[index[current]]
        if c[0] == 'set':
            reg[c[1]] = c[2] if isinstance(c[2], int) else reg[c[2]]
        elif c[0] == 'mul':
            reg[c[1]] *= c[2] if isinstance(c[2], int) else reg[c[2]]
        elif c[0] == 'add':
            reg[c[1]] += c[2] if isinstance(c[2], int) else reg[c[2]]
        elif c[0] == 'mod':
            a = c[2] if isinstance(c[2], int) else reg[c[2]]
            reg[c[1]] %= a
        elif c[0] == 'rcv':
            if len(snd) < 1:
                return False
            reg[c[1]] = snd.pop(0)
        elif c[0] == 'snd':
            if current == 1:
                index[2] += 1
            id.append((c[1] if isinstance(c[1], int) else reg[c[1]]))
        if c[0] == 'jgz':
            index[current] += (c[2] if isinstance(c[2], int) else reg[c[2]]) if (c[1] if isinstance(c[1], int) else reg[c[1]]) > 0 else 1
        else:
            index[current] += 1
        if index[current] < 0 or index[current] >= len(commands):
            return False
        return True
    while r1 or r2:
        if current == 0:
            r1 = runone(reg0, index, send0, send1)
            if not r1:
                current = 1
            else:
                r2 = True
        elif current == 1:
            r2 = runone(reg1, index, send1, send0)
            if not r2:
                current = 0
            else:
                r1 = True
    print 'part_2:', index[2]


part_2()


INPUT.close()
