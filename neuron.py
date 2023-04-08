#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

from random import random, randint
import re
import sys

from numeric import *

class Neuron:
    def __init__(self, weights = [], bias = 0):
        self.weights = [w for w in weights]
        self.bias = bias

class Synapse:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


if(__name__ == "__main__"):
    prog = None
    prev = None
    src = 'share/test.png'
    dest = 'share/output.png'
    rem = []
    for arg in sys.argv:
        if(prog == None):
            prog = arg
            continue
        if(prev == None):
            if(re.match(r'^-', arg) != None):
                prev = arg
                continue
            rem.append(arg)
            prev = None
            continue
        if(prev == '-i'):
            src = arg
            prev = None
            continue
        if(prev == '-o'):
            dest = arg
            prev = None
            continue
    print(f'Program: {prog}')
    print(f'Source: {src}')
    print(f'Destination: {dest}')
    print(f'Prev: {prev}')
    print(f'Remainder: {rem}')
