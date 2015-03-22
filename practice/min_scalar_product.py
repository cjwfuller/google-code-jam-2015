#!/usr/bin/env python3

"""
Solution to https://code.google.com/codejam/contest/32016/dashboard#s=p0

Works by doing computing all: x0ya + x1yb x2yc where x0..x2 are the values of
the first vector, ya..yc are the values of the second vector where a..c are all
permuations of the integers 0..n where n is the length of the two vectors
"""

import itertools

def find_min_scalar_product(vector_length, vector1, vector2):
    # initialse smallest
    smallest = 0
    for i in range(vector_length):
        smallest = smallest + vector1[i] * vector2[i]
    indices = list(range(vector_length))

    for perm in itertools.permutations(indices, vector_length):
        test_smallest = 0
        for i in range(vector_length):
            test_smallest = test_smallest + vector1[i] * vector2[perm[i]]
        if test_smallest < smallest:
            smallest = test_smallest
    return smallest

if __name__ == '__main__':
    num_cases = int(input())
    for x in range(num_cases):
        vector_length = int(input())
        vector1 = list(map(int, input().rstrip('\n').split(' ')))
        vector2 = list(map(int, input().rstrip('\n').split(' ')))
        smallest = find_min_scalar_product(vector_length, vector1, vector2)
        print("Case #" + str(x + 1) + ": " + str(smallest))
