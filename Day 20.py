# Particle Swarm
import re
import math
INPUT = open('Day 20.txt', 'r')
pos = 10000000000000
par = -1
time = 100000
i = 0
for line in INPUT:
    data = re.findall('\d+', line)
    x = int(data[0]) + int(data[3]) * time + 0.5 * int(data[6]) * time * time
    y = int(data[1]) + int(data[4]) * time + 0.5 * int(data[7]) * time * time
    z = int(data[2]) + int(data[5]) * time + 0.5 * int(data[8]) * time * time
    sm = abs(x) + abs(y) + abs(z)
    if sm < pos:
        par = i
        pos = sm
    i += 1
print 'part_1:', par

INPUT.close()

INPUT = open('Day 20.txt', 'r')
i = 0
parts = {}
for line in INPUT:
    data = re.findall('-?\d+', line)
    parts[i] = [int(h) for h in data if h != '']
    i += 1
for j in xrange(10000):
    points = {}
    for p in parts:
        data = parts[p]
        data[3] += data[6]
        data[0] += data[3]
        data[4] += data[7]
        data[1] += data[4]
        data[5] += data[8]
        data[2] += data[5]
        asd = str(data[0:3])
        if asd in points:
            points[asd].append(p)
        else:
            points[asd] = [p]
    for p in points:
        if len(points[p]) > 1:
            for a in points[p]:
                del parts[a]

print 'part_2:', len(parts)

INPUT.close()
