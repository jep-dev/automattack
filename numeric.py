#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

from math import *

def clamp(x, lo = 0, hi = 1):
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

def aton(src):
    x = src.lower()
    x = ''.join(x.split())
    f = atof(x)
    if('.' in x):
        return f
    if('inf' in x or 'nan' in x):
        return f
    return atoi(x)

def logistic(x):
    return 1/(1+exp(-x))
def dlogistic(x):
    y = exp(-x)
    return x*y/pow(1+y, 2)
def ilogistic(x):
    return log(exp(x)+1)

# linear at s=0
def hyperbolic(x, s = 2, m = 1.0):
    y = float(clamp(x, 0, m))/m
    return sqrt(y*(y+s)/(1+s))*m
