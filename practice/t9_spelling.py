#!/usr/bin/env python3

"""
Solution to https://code.google.com/codejam/contest/351101/dashboard#s=p2
"""

t9_map = {
    ' ': '0',
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999'
}

def words_to_numbers(words):
    numbers = ''
    for idx, w in enumerate(words):
        if idx != 0 and t9_map[w][0] == t9_map[words[idx - 1]][0]:
            numbers = numbers + ' '
        numbers = numbers + t9_map[w]
    return numbers

if __name__ == '__main__':
    num_cases = int(input())
    for x in range(0, num_cases):
        words = input()
        sequence = words_to_numbers(words)
        print("Case #" + str(x + 1) + ": " + sequence)
