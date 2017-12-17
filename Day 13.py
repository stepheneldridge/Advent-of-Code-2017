# Digital plumber
import re
INPUT = open('Day 13.txt', 'r')
everything = {}
for line in INPUT:
    nums = re.findall('\d+', line)
    everything[int(nums[0])] = {'r': int(nums[1]), 's': 0}
score = 0
for i in xrange(91):
    if i in everything and everything[i]['s'] == 0:
        score += i * everything[i]['r']
    for j in everything:
        r = everything[j]['r'] - 1
        everything[j]['s'] = r - abs(((i + 1) % (2 * r)) - r)

print 'part_1:', score

x = 0
while True:
    score = 0
    for j in everything:
        r = everything[j]['r'] - 1
        if r - abs(((j + x) % (2 * r)) - r) == 0:
            score += 1
            break
    if score == 0:
        print 'part_2:', x
        break
    x += 1
INPUT.close()
