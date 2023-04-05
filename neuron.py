#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

from rand import random, randint

def progress(i, i0, i1):
    assert i0 < i1
    return (i - i0) / float(i1 - i0)

if(__name__ == "__main__"):
    w,h = [4,3]

    seeded = False
    seed = -1
    if(len(argv) > 1):
        seeded = True
        seed = int(argv[1])
        rand.seed(seed)

    print(f'Seeded={seeded}, seed={seed}')

    m = w*h
    n = m*2
    img0 = [random() for i in range(m*4)]
    imgh = [[random() for i in range(m*4)] for j in range(2)]
    img1 = [0 for i in range(m*4)]


