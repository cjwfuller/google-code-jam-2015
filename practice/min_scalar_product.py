#!/usr/bin/env python3

"""Solution to https://code.google.com/codejam/contest/32016/dashboard#s=p0"""

if __name__ == '__main__':
    num_cases = int(input())
    for x in range(num_cases):
        vector_length = int(input())
        vector1 = list(map(int, input().rstrip('\n').split(' ')))
        vector2 = list(map(int, input().rstrip('\n').split(' ')))
        vector1.sort()
        vector2.sort()
        smallest = 0
        for i in range(vector_length):
            smallest = smallest + vector1[i] * vector2[vector_length - i - 1]
        print("Case #" + str(x + 1) + ": " + str(smallest))
