# Knot hash


def part_1():
    INPUT = [165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153]
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

    for i in INPUT:
        flip(pos, pos + i)
        pos = (pos + skip + i) % 256
        skip += 1
    print 'part_1:', arr[0] * arr[1]


def part_2():
    INPUT = '165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153'
    new_i = []
    for i in INPUT:
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
    print 'part_2:', ''.join([hx(i) for i in dense])


part_1()
part_2()
