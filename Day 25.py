#
step = 12134527
state = 'A'
tape = {}
current = 0
taken = 0


def get_v(s, data):
    if s in data:
        return data[s]
    else:
        data[s] = 0
        return data[s]


for i in xrange(step):
    if state == 'A':
        if get_v(current, tape) == 0:
            tape[current] = 1
            current += 1
            state = 'B'
        else:
            tape[current] = 0
            current -= 1
            state = 'C'
    elif state == 'B':
        if get_v(current, tape) == 0:
            tape[current] = 1
            current -= 1
            state = 'A'
        else:
            tape[current] = 1
            current += 1
            state = 'C'
    elif state == 'C':
        if get_v(current, tape) == 0:
            tape[current] = 1
            current += 1
            state = 'A'
        else:
            tape[current] = 0
            current -= 1
            state = 'D'
    elif state == 'D':
        if get_v(current, tape) == 0:
            tape[current] = 1
            current -= 1
            state = 'E'
        else:
            tape[current] = 1
            current -= 1
            state = 'C'
    elif state == 'E':
        if get_v(current, tape) == 0:
            tape[current] = 1
            current += 1
            state = 'F'
        else:
            tape[current] = 1
            current += 1
            state = 'A'
    elif state == 'F':
        if get_v(current, tape) == 0:
            tape[current] = 1
            current += 1
            state = 'A'
        else:
            tape[current] = 1
            current += 1
            state = 'E'
count = 0
for key in tape:
    if tape[key] == 1:
        count += 1
print count
