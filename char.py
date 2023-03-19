#!/usr/bin/env python3

from copy import copy, deepcopy
from util import *

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Stats:
    def __init__(self, ARM=0, DEX=0, HP=0, \
            INV=0, INT=0, MR=0, STR=0):
        self.ARM = clamp(4+ARM)
        self.DEX = clamp(10+DEX)
        self.HP = clamp(100+HP)
        self.INV = clamp(10+INV)
        self.INT = clamp(10+INT)
        self.MR = clamp(10+MR)
        self.STR = clamp(10+STR)

class Char:
    name = "Greg"
    kin = "base"
    stats = None
    base_stats = None
    target = None

    def __str__(self):
        return f'{self.name} the {self.kin}'
    def __init__(self, name, kin, stats = Stats()):
        self.name = name
        self.kin = kin
        self.stats = stats
        self.base_stats = deepcopy(self.stats)

class Human(Char):
    def __init__(self, name):
        super().__init__(name, "human")

class Orc(Char):
    def __init__(self, name):
        super().__init__(name, "orc", Stats(
            1, 0, 0, 1, -2, -2, 2))

class Elf(Char):
    def __init__(self, name):
        super().__init__(name, "elf", Stats(
            1, 1, 1, -1, 0, 2, -1))

class Goblin(Char):
    def __init__(self, name):
        super().__init__(name, "goblin", Stats(
            -1, 2, -60, 1, -3, -1, -1))

def dead(c):
    t = type(c)
    if(issubclass(t, Stats)):
        return c.HP <= 0 or c.INT <= 0
    if(issubclass(t, Char)):
        return dead(c.stats)
    for ci in c:
        if(alive(ci)):
            return False
    return True

def alive(c):
    return not dead(c)

def die(c):
    t = type(c)
    if(issubclass(t, Stats)):
        c.HP = 0
        c.INV = 0
    elif(issubclass(t, Char)):
        die(c.stats)
        c.target = None
    elif(isanysubclass(t, list, tuple)):
        for ci in c:
            die(ci)
    else:
        return False
    return True

