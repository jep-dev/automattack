#!/usr/bin/env python3

from char import *
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"


class Team:
    life = []
    death = []

    def append(self, elem):
        if(elem == None or not alive(elem)):
            death.append(elem)
            return self
        life.append(elem)
        return self

    def store(self, i):
        return self.death.append(self.life.pop(i))
    def load(self, i):
        return self.life.append(self.death.pop(i))
    def empty(self):
        return len(life) == 0
    def __init__(self, *args):
        for arg in args:
            if arg == None or not alive(arg):
                death.append(arg)
            else:
                life.append(arg)
