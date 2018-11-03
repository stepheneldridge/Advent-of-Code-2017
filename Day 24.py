# Electromagnetic moat
INPUT = open('Day 24.txt', 'r')
ports = []
for line in INPUT:
    num = line[:-1].split('/')
    ports.append(num)
def find(a, nb, data):
    vals = {}
    for i in xrange(len(data)):
        if i in nb:
            continue
        if a in data[i]:
            b = data[i][0]
            if a == b:
                b = data[i][1]
            sm = int(a) + int(b)
            chil = find(b, nb + [i], data)
            m = max([int(chil[h]['sum']) for h in chil] + [0])
            vals[i] = {'c': chil, 'sum': sm + m}
    return vals

need = '0'
a = find(need, [], ports)
print 'part_1:', max([a[i]['sum'] for i in a])
def part_2():
    w = [0, 0]
    def find(a, nb, data, s, w):
        if len(nb) >= w[1]:
            w[1] = len(nb)
            if s > w[0]:
                w[0] = s
        vals = {}
        for i in xrange(len(data)):
            if i in nb:
                continue
            if a in data[i]:
                b = data[i][0]
                if a == b:
                    b = data[i][1]
                sm = int(a) + int(b)
                chil = find(b, nb + [i], data, s + sm, w)
                vals[i] = chil
        return vals
    find('0', [], ports, 0, w)
    print 'part_2:', w[0]
part_2()


