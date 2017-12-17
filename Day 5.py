# Jump Maze
INPUT = open('Day 5.txt', 'r')


def part_1():
    arr = [int(i) for i in INPUT]
    index = 0
    it = 0
    while index < len(arr) and index >= 0:
        a = index
        index += arr[a]
        arr[a] += 1
        it += 1
    print it


def part_2():
    arr = [int(i) for i in INPUT]
    index = 0
    it = 0
    while index < len(arr) and index >= 0:
        a = index
        index += arr[a]
        arr[a] += 1 if arr[a] < 3 else -1
        it += 1
    print it


part_1()
INPUT.close()
INPUT = open('Day 5.txt', 'r')
part_2()
INPUT.close()
