#!/usr/bin/env python3

import sys

"""Solution to https://code.google.com/codejam/contest/32016/dashboard#s=p1"""

def flavour_used(flavour, all_likes):
    found = False
    for l in range(1, len(all_likes), 2):
        if flavour == l:
            found = True
    return found

def is_malted(flavour, all_likes):
    return True

def satisfy(num_flavours, all_likes):
    if not can_satisfy(num_flavours, all_likes):
        print("IMPOSSIBLE")
    else:
        for f in range(1, num_flavours + 1):
            malted = is_malted(f, all_likes)
            if not flavour_used(f, all_likes) or not malted:
                sys.stdout.write("0 ")
            else:
                sys.stdout.write("1 ")
        print()

if __name__ == '__main__':
    num_cases = int(input())
    for x in range(num_cases):
        all_likes = []
        num_flavours = int(input())
        num_customers= int(input())
        for y in range(num_customers):
            likes = list(map(int, input().rstrip('\n').split(' ')))
            num_likes = int(likes[0])
            likes = likes[1:]
            all_likes = all_likes + likes
        print("Case #" + str(x + 1) + ": ", end="", flush=True)
        satisfy(num_flavours, all_likes)
