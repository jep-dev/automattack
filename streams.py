#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

import io
import re
import sys

from util import *
from timing import *
from functional import *

def yesman(*y, **z):
    return True
def iscomment(src, *y, **z):
    return re.match(r'^\s*#', src) != None

def trim(src, to = ''):
    return re.sub(r'^\s+|\s+$', to, src)
def compress(src, to = ' ', pat = r'\S+'):
    return to.join(re.findall(pat, src))
def noncomment(src):
    return re.sub(r'\s*#.*', '', src)


def lines(fname, dest = [], pred = yesman, fn = identity):
    f = io.open(fname)
    for l in f:
        if(pred(l)):
            dest.append(fn(l))
    f.close()
    return dest

if(__name__ == '__main__'):
    i = 0
    coms = []
    noncoms = []
    fname = 'share/test.txt'
    lines(fname, noncoms, yesman, noncomment)
    #lines(fname, noncoms, fnot(iscomment))
    #

    for line in noncoms:
        i = i + 1
        print(f'{i}. "{line[0:-1]}"')
    sys.exit(0)

