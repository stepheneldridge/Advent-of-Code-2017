# Spinlock
skip = 367
arr = [0]
spot = 0
for i in xrange(2017):
    spot = ((spot + skip) % len(arr)) + 1
    arr.insert(spot, i + 1)
print 'part_1:', arr[(spot + 1) % len(arr)]
after = []
for i in xrange(50000000 - 1):
    spot = ((spot + skip) % (i + 1)) + 1
    if spot == 1:
        after.append(i + 1)
print 'part_2:', max(after)
