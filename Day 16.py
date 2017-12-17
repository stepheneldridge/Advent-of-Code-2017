#
import re
INPUT = open('Day 16.txt', 'r')
start = list('abcdefghijklmnop')


def spin(data, amount):
    return data[-amount:] + data[0:-amount]


def swap_pos(data, a, b):
    tmp = data[a]
    data[a] = data[b]
    data[b] = tmp
    return data


def swap_val(data, a, b):
    return swap_pos(data, data.index(a), data.index(b))


for line in INPUT:
    commands = re.split(',', line)
    funs = []
    for c in commands:
        ints = re.findall('\d+', c)
        if c[0] == 's':
            funs.append(['s', int(ints[0])])
        elif c[0] == 'x':
            funs.append(['x', int(ints[0]), int(ints[1])])
        elif c[0] == 'p':
            funs.append(['p', c[1], c[3]])
    start2 = list('abcdefghijklmnop')
    for c in funs:
        if c[0] == 's':
            start2 = spin(start2, c[1])
        elif c[0] == 'x':
            start2 = swap_pos(start2, c[1], c[2])
        elif c[0] == 'p':
            start2 = swap_val(start2, c[1], c[2])
    print 'part_1:', ''.join(start2)
    start1 = list('abcdefghijklmnop')
    loop = 1
    for wan in xrange(1000000000):
        for c in funs:
            if c[0] == 's':
                start = spin(start, c[1])
            elif c[0] == 'x':
                start = swap_pos(start, c[1], c[2])
            elif c[0] == 'p':
                start = swap_val(start, c[1], c[2])
        if start == start1:
            loop = wan + 1
            break
    for wan in xrange(1000000000 % loop):
        for c in funs:
            if c[0] == 's':
                start = spin(start, c[1])
            elif c[0] == 'x':
                start = swap_pos(start, c[1], c[2])
            elif c[0] == 'p':
                start = swap_val(start, c[1], c[2])


print 'part_2:', ''.join(start)
INPUT.close()
