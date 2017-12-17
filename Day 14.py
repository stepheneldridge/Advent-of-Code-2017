# Disk defragmentation
INPUT = 'hwlqcszp'


def hash(input):
    new_i = []
    for i in input:
        new_i.append(ord(i))
    new_i.extend([17, 31, 73, 47, 23])
    arr = [i for i in xrange(256)]
    skip = 0
    pos = 0

    def flip(a, b):
        ar = []
        for i in xrange(b - a):
            ar.append(arr[(i + a) % 256])
        ar.reverse()
        for i in xrange(b - a):
            arr[(i + a) % 256] = ar[i]
    for j in xrange(64):
        for i in new_i:
            flip(pos, pos + i)
            pos = (pos + skip + i) % 256
            skip += 1
    dense = []
    for i in xrange(16):
        dense.append(arr[i * 16])
        for j in xrange(15):
            dense[i] = dense[i] ^ arr[(i * 16) + j + 1]

    def hx(a):
        b = hex(a)[2:]
        if len(b) == 1:
            b = '0' + b
        return b
    return ''.join([hx(i) for i in dense])


rows = []
for i in xrange(128):
    rows.append(hash(INPUT + '-' + str(i)))
    rows[i] = str(bin(int(rows[i], 16)))[2:].count('1')

print 'part_1:', sum(rows)

rows = []
for i in xrange(128):
    rows.append(hash(INPUT + '-' + str(i)))
    rows[i] = list(str(bin(int(rows[i], 16)))[2:])
    rows[i] = ['0' for j in xrange(128 - len(rows[i]))] + rows[i]


def rm_adj(x, y):
    if x >= 0 and x < 128 and y >= 0 and y < 128 and rows[x][y] == '1':
        rows[x][y] = '0'
    else:
        return
    rm_adj(x + 1, y)
    rm_adj(x, y + 1)
    rm_adj(x - 1, y)
    rm_adj(x, y - 1)


total = 0
for i in xrange(128):
    for j in xrange(128):
        if rows[i][j] == '1':
            rm_adj(i, j)
            total += 1

print 'part_2:', total
