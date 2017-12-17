# Passphrase
import re
INPUT = open('Day 4.txt', 'r')


def part_1():
    total_valid = 0
    for line in INPUT:
        words = re.split('\s', line)
        if len(words) == len(set(words)):
            total_valid += 1
    print total_valid


def part_2():
    total_valid = 0
    for line in INPUT:
        words = re.split('\s', line)
        if anagram_in_phrase(words):
            continue
        total_valid += 1
    print total_valid


def anagram_in_phrase(words):
    for i, word in enumerate(words[:-1]):
        for word_2 in words[i + 1:]:
            if is_anagram(word, word_2):
                return True
    return False


def is_anagram(a, b):
    if len(a) != len(b):
        return False
    for i, v in enumerate(a):
        if a.count(v) != b.count(v):
            return False
    return True


part_1()
INPUT.close()
INPUT = open('Day 4.txt', 'r')
part_2()
INPUT.close()
