#!/usr/bin/env python3

from time import sleep
from sys import stdout

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def timed(*objs, sep=' ', end='\n', file=stdout, flush=False):
    print(*objs, sep=sep, end=end, file=file, flush=flush)
    sleep(1.5)
