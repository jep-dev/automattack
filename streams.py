#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

import io
from util import *
from timing import *

def emptyline(s):
    return len(s) == 0 or s[0] == '#'

def lines(fname):
    f = io.open(fname)
    out = [line for line in f if not emptyline(line)]
    f.close()
    return out
