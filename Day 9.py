# Stream processing
INPUT = open('Day 9.txt', 'r')
negate = False
garbage = False
score = 0
depth = 0
count = 0
for line in INPUT:
    for char in line:
        if negate:
            negate = False
            continue
        if garbage and char != '>' and char != '!':
            count += 1
            continue
        if char == '<':
            garbage = True
        elif char == '>':
            garbage = False
        elif char == '{':
            depth += 1
            score += depth
        elif char == '}':
            depth -= 1
        elif char == '!':
            negate = True
print 'part_1:', score
print 'part_2:', count
INPUT.close()
