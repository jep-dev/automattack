#!/usr/bin/env python3

from char import *
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"


class Team:
    front = [] # living & undead
    back = [] # dead
    def __getitem__(self, k):
        if(k==0):
            return front
        else:
            return back
    def __setitem__(self, k, v):
        if(k==0):
            return front = v
        else:
            return back = v
    def shelf(self, i):
        return self.back.append(self.front.pop(i))
    def unshelf(self, i):
        return self.front.append(self.back.pop(i))
