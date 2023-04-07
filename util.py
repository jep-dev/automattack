#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

import math
import re
import sys

from numeric import *

def ltcompare(l, r):
    return l < r

def compare(l, r, f = ltcompare):
    if(l < r):
        return -1
    if(r < l):
        return 1
    return 0

def ispsubclass(l, r):
    if(issubclass(l, r)):
        return not issubclass(r, l)
    return False

def test_util():
    isa = lambda x,y : type(x) == y
    isint = lambda x : isa(x, int)
    isfloat = lambda x : isa(x, float)

    ints = ['-1', '+1']
    nones = ['', '.', '-', '+', '0x']
    floats = ['-nan', '-inf', '-0.', '.0', 'inf', 'nan']

    for n in nones:
        assert atof(n) == None
        assert atoi(n) == None
        assert aton(n) == None

    for n in ints:
        assert isint(atoi(n))
        assert isfloat(atof(n))
        assert isint(aton(n))

    for n in floats:
        assert atoi(n) == None
        assert isfloat(atof(n))
        assert isfloat(aton(n))

    return True

if(__name__ == "__main__"):
    print('Testing util.py;')
    if(test_util()):
        print('Test passed.')
        sys.exit(0)
    print('Test failed.')
    sys.exit(1)
