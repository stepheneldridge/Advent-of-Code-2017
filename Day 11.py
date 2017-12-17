# Hex grid
import math
INPUT = open('Day 11.txt', 'r')
for line in INPUT:
    cats = ['ne', 'nw', 'n']  # line.split('\n')[0].split(',')
    up = cats.count('n') - cats.count('s')
    ne = cats.count('ne') - cats.count('sw')
    nw = cats.count('nw') - cats.count('se')
    order = [up, ne, nw]
    order.sort()
    print 'part_1:', math.sqrt(abs((up + nw / 2.0) ** 2.0 + (ne - nw / 2.0) ** 2.0))
    break
    m = 0
    for i in xrange(len(cats)):
        cat = cats[:i]
        up = abs(cat.count('n') - cat.count('s'))
        ne = abs(cat.count('ne') - cat.count('sw'))
        nw = abs(cat.count('nw') - cat.count('se'))
        order = [up, ne, nw]
        order.sort()
        m = max(m, sum(order[1:]))
    print 'part_2:', m


INPUT.close()
# WRONG
# part_1: 743
# part_2: 1493
