#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def clamp(x, lo = 0, hi = 20):
    lo2 = min(lo, hi)
    hi2 = max(lo, hi)
    return min(max(lo2, x), hi2)

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

def aton(x):
    f = atof(x)
    i = atoi(x)
    if(i == f):
        return i
    return f
