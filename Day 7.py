# Recursive Circus
import re
INPUT = open('Day 7.txt', 'r')


def part_1():
    print 'part 1:'
    unique = set()
    singles = {}
    for i in INPUT:
        mat = re.findall('[A-Za-z]+', i)
        unique.update(mat)
        singles[mat[0]] = set(mat[1:]) if len(mat) > 1 else []
    print find(unique.pop(), singles)


def find(x, data):
    for i in data:
        if x in data[i]:
            return find(i, data)
    return x


def part_2():
    print 'part 2:'
    unique = {}
    singles = {}
    for i in INPUT:
        mat = re.findall('[A-Za-z]+', i)
        weight = re.search('[0-9]+', i).group(0)
        unique[mat[0]] = int(weight)
        singles[mat[0]] = mat[1:] if len(mat) > 1 else []
    print find('azqje', singles)
    # build tree
    tree = {'azqje': {'weight': 0, 'children': {}}}
    for i in singles['azqje']:
        tree['azqje']['children'][i] = build(i, unique, singles)
    print tree
    for i in tree['azqje']['children']['inwmb']['children']['nzeqmqi']['children']['rfkvap']['children']:
        print i
        print sumbranch(tree['azqje']['children']['inwmb']['children']['nzeqmqi']['children']['rfkvap']['children'][i])  # 9 too high
    print unique['rfkvap']


def build(start, weights, data):
    tmp = {
        'weight': weights[start],
        'children': {i: build(i, weights, data) for i in data[start]} if len(data[start]) > 0 else {}
    }
    return tmp


def sumbranch(branch):
    sm = 0
    sm += branch['weight']
    if 'children' not in branch:
        return sm
    sm += sum([sumbranch(branch['children'][i]) for i in branch['children']])
    return sm


part_1()
INPUT.close()
INPUT = open('Day 7.txt', 'r')
part_2()
INPUT.close()
print 'done'
