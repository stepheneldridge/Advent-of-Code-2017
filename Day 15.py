# Dueling generators


def part_1():
    a = 516
    b = 190
    c = 2 ** 16
    tot = 0
    for i in xrange(40000000):
        a *= 16807
        b *= 48271
        a %= 2147483647
        b %= 2147483647
        if a % c == b % c:
            tot += 1
    print tot


def part_2():
    a = 516
    b = 190
    c = 2 ** 16
    tot = 0
    al = []
    bl = []

    while len(al) < 5000000:
        a *= 16807
        a %= 2147483647
        if a % 4 == 0:
            al.append(a)
    print 'cry'
    while len(bl) < 5000000:
        b *= 48271
        b %= 2147483647
        if b % 8 == 0:
            bl.append(b)
    for i in xrange(min(len(al), len(bl))):
        if al[i] % c == bl[i] % c:
            tot += 1
    print tot


part_2()
