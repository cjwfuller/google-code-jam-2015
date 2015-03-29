#!/usr/bin/env python3

import sys

"""Solution to https://code.google.com/codejam/contest/32016/dashboard#s=p1"""

def still_possible(like):
    """Are there flavours that have not been selected or match customer's choice

    Arguments:
    like -- e.g. [1, 0, 2, 0]
    """
    it = iter(like)
    for x in it:
        posn = x
        malted = next(it)
        if flavours[posn] == -1 or flavours[posn] == malted:
            return True
    return False

def satisfy(num_flavours, all_likes):
    """Try to satisfy a customer with milkshake

    Arguments:
    num_flavours - number of flavours of milkshake
    all_likes - e.g. [[1, 0], [0, 1]]
    """
    # build an empty dict of flavour => is_malted
    for x in range(num_flavours):
        flavours[x + 1] = -1
    # attempt to satisfy
    for like in all_likes:
        it = iter(like)
        for x in it:
            posn = x
            malted = next(it)
            if flavours[posn] == -1 or flavours[posn] == malted:
                flavours[posn] = malted
            elif not still_possible(like):
                print("IMPOSSIBLE")
                return
    for idx, val in enumerate(flavours):
        if flavours[idx + 1] == -1:
            flavours[idx + 1] = 0
        sys.stdout.write(str(flavours[idx + 1]) + " ")
    print()

if __name__ == "__main__":
    num_cases = int(input())
    for x in range(num_cases):
        flavours = {}
        num_flavours = int(input())
        num_customers = int(input())
        all_likes = []
        for y in range(num_customers):
            likes = list(map(int, input().rstrip('\n').split(' ')))
            all_likes = all_likes + [likes[1:]]
        print("Case #" + str(x + 1) + ": ", end="", flush=True)
        satisfy(num_flavours, all_likes)
