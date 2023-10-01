#!/usr/bin/python3

import sys
from rd_data import rd_data

data = rd_data(sys.argv[1])
maxi = max(data)
mini = min(data)


def pr_gen():

    pN = []
    for v in range(2, 100):
        if v > 1:
            for x in range(2, v):
                if (v % x) == 0:
                    break
            else:
                pN.append(v)
    return (pN)


prN = pr_gen()


def g_mul(d, e):
    for x in range(len(d)):
        for y in range(len(e)):
            if d[x] % e[y] == 0:
                xe = d[x] // e[y]
                print("{}={}*{}".format(d[x], xe, e[y]))
                break


g_mul(data, prN)
