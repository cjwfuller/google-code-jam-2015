#!/usr/bin/env python3

"""
Solution to https://code.google.com/codejam/contest/351101/dashboard#s=p0
"""

import itertools

def get_indices(credit, prices):
    indices = list(range(len(prices)))
    for subset in itertools.combinations(indices, 2):
        total = prices[subset[0]] + prices[subset[1]]
        if total == credit:
            return str(subset[0] + 1) + ' ' + str(subset[1] + 1)

if __name__ == '__main__':
    count = 0
    num_cases = int(input())
    while count < num_cases:
        credit = int(input())
        num_items = int(input())
        prices = list(map(int, input().rstrip('\n').split(' ')))
        indices = get_indices(credit, prices)
        print("Case #" + str(count) + ": " + indices)
        count = count + 1
