#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def clamp(x, lo = 0, hi = 20):
    if(lo > hi):
        return min(max(hi, x), lo)
    return min(max(lo, x), hi)

