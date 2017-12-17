# Registers
import re
INPUT = open('Day 8.txt', 'r')
reg = {}


def check(slot, op, val):
    if slot not in reg:
        ch = 0
    else:
        ch = reg[slot]
    if op == '!=':
        return ch != val
    if op == '==':
        return ch == val
    if op == '<=':
        return ch <= val
    if op == '>=':
        return ch >= val
    if op == '<':
        return ch < val
    if op == '>':
        return ch > val
    print 'failed:', op


n = 0
for line in INPUT:
    data = re.split('\s+', line)
    if data[0] not in reg:
        reg[data[0]] = 0
    doif = check(data[4], data[5], int(data[6]))
    inc = int(data[2]) * (-1 if data[1] == 'dec' else 1)
    reg[data[0]] += inc if doif else 0
    n = max(n, reg[data[0]])

m = 0
for i in reg:
    m = max(m, reg[i])
print 'part_1:', m

print 'part_2:', n

INPUT.close()
