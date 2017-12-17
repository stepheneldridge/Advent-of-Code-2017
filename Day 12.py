# Digital plumber
import re
INPUT = open('Day 12.txt', 'r')
everything = {}
for line in INPUT:
    things = re.findall('\d+', line)
    everything[things[0]] = things[1:]


def ain(st, d):
    st.add(d)
    for i in everything[d]:
        if i not in st:
            ain(st, i)
    return st


print 'part_1:', len(ain(set(), '0'))
tot = 0
s = set()
for i in everything:
    if i not in s:
        tot += 1
        s.update(ain(set(), i))
print 'part_2:', tot
INPUT.close()
