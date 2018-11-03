# Sporifica Virus
import re
INPUT = open('Day 23.txt', 'r')
commands = []
reg = {}
reg0 = {}
reg1 = {}
for line in INPUT:
    stuff = re.split('\s+', line)
    try:
        stuff[1] = int(stuff[1])
    except Exception:
        reg[stuff[1]] = 0
        reg0[stuff[1]] = 0
        reg1[stuff[1]] = 1
    try:
        stuff[2] = int(stuff[2])
    except Exception:
        reg[stuff[2]] = 0
        reg0[stuff[2]] = 0
        reg1[stuff[2]] = 1
    commands.append(stuff)

index = 0
count = 0
while True:
    c = commands[index]
    if c[0] == 'set':
        reg[c[1]] = c[2] if isinstance(c[2], int) else reg[c[2]]
    elif c[0] == 'mul':
        reg[c[1]] *= c[2] if isinstance(c[2], int) else reg[c[2]]
        count += 1
    elif c[0] == 'sub':
        reg[c[1]] -= c[2] if isinstance(c[2], int) else reg[c[2]]
    if c[0] == 'jnz':
        index += (c[2] if isinstance(c[2], int) else reg[c[2]]) if (c[1] if isinstance(c[1], int) else reg[c[1]]) != 0 else 1
    else:
        index += 1
    if index < 0 or index >= len(commands):
        break
print count
h = 0
b = 99 * 100 + 100000
for x in range(b ,b + 17000 + 1,17):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break
print h
