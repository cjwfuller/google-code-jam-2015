#!/usr/bin/env python3

"""
Solution to https://code.google.com/codejam/contest/32016/dashboard#s=p0

Works by doing computing all: x0ya + x1yb x2yc where x0..x2 are the values of
the first vector, ya..yc are the values of the second vector where a..c are all
permuations of the integers 0..n where n is the length of the two vectors
"""

import itertools

if __name__ == '__main__':
    num_cases = int(input())
    for x in range(num_cases):
        vector_length = int(input())
        vector1 = list(map(int, input().rstrip('\n').split(' ')))
        vector2 = list(map(int, input().rstrip('\n').split(' ')))

        # initialse smallest
        smallest = 0
        for i in range(vector_length):
            smallest = smallest + vector1[i] * vector2[i]

        # find Minimum Scalar Product
        indices = list(range(vector_length))
        triples = itertools.permutations(indices, vector_length)
        for t in triples:
            test_smallest = 0
            for i in range(vector_length):
                test_smallest = test_smallest + vector1[i] * vector2[t[i]]
            if test_smallest < smallest:
                smallest = test_smallest
        print("Case #" + str(x + 1) + ": " + str(smallest))
