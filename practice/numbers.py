#!/usr/bin/env python3

import math

"""
Solution to https://code.google.com/codejam/contest/32016/dashboard#s=p2
"""

if __name__ == "__main__":
    num_cases = int(input())
    for count in range(1, num_cases + 1):
        n = int(input())
        if n >= 20:
            ans = "625"
        else:
            res = str(pow((3 + math.sqrt(5)), n))

            index = res.index('.')
            start = index - 3
            if start < 0:
                start = 0

            ans = res[start:index]
            while len(ans) != 3:
                ans = '0' + ans
        print("Case #" + str(count) + ": " + ans)
