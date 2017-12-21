# Fractal art
INPUT = open('Day 21.txt', 'r')
rules = {}
start = '.#./..#/###'
for line in INPUT:
    r = line[:-1].split(' => ')
    rules[r[0]] = r[1]


def findRule(s, rules):
    tmp = s
    def rot(st):
        if len(st) == 5:
            return st[3] + st[0] + st[2] + st[4] + st[1]
        else:
            return st[8] + st[4] + st[0] + st[3] + st[9] + st[5] + st[1] + st[7] + st[10] + st[6] + st[2]
    def flip(st):
        if len(st) == 5:
            return st[3:] + st[2] + st[0:2]
        else:
            return st[8:] + st[3] + st[4:7] + st[7] + st[0:3]
    for a in xrange(2):
        for b in xrange(4):
            if tmp in rules:
                return rules[tmp]
            tmp = rot(tmp)
        tmp = flip(tmp)

def magic(st, s):
    fin = []
    for x in xrange(len(st)):
        for k in xrange(s):
            fin.append('')
            for y in xrange(len(st[x])):
                fin[x*s+k] += st[x][y].split('/')[k]
    return fin


def solve(iter):
    data = start.split('/')
    for i in xrange(iter):
        size = len(data)
        new = []
        if size % 2 == 0:
            for x in xrange(size / 2):
                new.append([])
                for y in xrange(size / 2):
                    new[x].append(findRule(data[2*x][2*y: 2*(y+1)] + '/' + data[2*x + 1][2*y: 2*(y+1)], rules))
            data = magic(new, 3)
        else:
            for x in xrange(size / 3):
                new.append([])
                for y in xrange(size / 3):
                    new[x].append(findRule(data[3*x][3*y: 3*(y+1)] + '/' + data[3*x + 1][3*y: 3*(y+1)] + '/' + data[3*x + 2][3*y: 3*(y+1)], rules))
            data = magic(new, 4)
    return ''.join(data).count('#')

print 'part_1:', solve(5)
print 'part_2:', solve(18)
INPUT.close()
