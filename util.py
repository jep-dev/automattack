#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

import math
import re

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

def clamp(x, lo = 0, hi = 1):
    lo2 = min(lo, hi)
    hi2 = max(lo, hi)
    return min(max(lo2, x), hi2)

def trim(src, to = ''):
    return re.sub(r'^\W+|\W+$', to, src)

def compress(src, to = ''):
    return re.sub(r'\W+', to, src)

def atoi(x):
    try:
        return int(x)
    except ValueError:
        return None

def atof(x):
    try:
        return float(x)
    except ValueError:
        return None

def aton(src):
    x = src.lower()
    x = ''.join(x.split())
    f = atof(x)
    if('.' in x):
        return f
    if('inf' in x or 'nan' in x):
        return f
    return atoi(x)

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
