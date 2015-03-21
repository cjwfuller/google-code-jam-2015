#!/usr/bin/env python3

"""
Solution to https://code.google.com/codejam/contest/351101/dashboard#s=p1
"""

def reverse_words(words):
    words = words.split(' ')
    count = 0
    num_words = len(words)
    while count < round(num_words / 2):
        tmp = words[count]
        words[count] = words[num_words - count - 1]
        words[num_words - count - 1] = tmp
        count = count + 1
    return words

if __name__ == '__main__':
    num_cases = int(input())
    for x in range(0, num_cases):
        words = input()
        reversed_words = reverse_words(words)
        reversed_words = ' '.join(reversed_words)
        print("Case #" + str(x + 1) + ": " + reversed_words)
