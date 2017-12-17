# Memory Reallocation
import re
INPUT = open('Day 6.txt', 'r')


def part_1():
    seen = []
    for i in INPUT:
        words = re.split('\s+', i)
        words = [int(x) for x in words if x is not '']
        it = 0
        while str(words) not in seen:
            seen.append(str(words))
            m = max(words)
            index = words.index(m)
            words[index] = 0
            for j in xrange(m):
                index = (index + 1) % len(words)
                words[index] += 1

            it += 1
    print it


def part_2():
    seen = []
    for i in INPUT:
        words = re.split('\s+', i)
        words = [int(x) for x in words if x is not '']
        it = 0
        while str(words) not in seen:
            seen.append(str(words))
            m = max(words)
            index = words.index(m)
            words[index] = 0
            for j in xrange(m):
                index = (index + 1) % len(words)
                words[index] += 1

            it += 1
    print it - seen.index(str(words))


part_1()
INPUT.close()
INPUT = open('Day 6.txt', 'r')
part_2()
INPUT.close()
# 6681, 2392
