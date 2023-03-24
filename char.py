#!/usr/bin/env python3

from copy import copy, deepcopy
from util import *

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Stats:
    def __init__(self, ARM = 0, DEX = 0, HP = 0, \
            INV = 0, INT = 0, MR = 0, STR = 0):
        self.ARM = 4 + clamp(ARM, -4, 16)
        self.DEX = 10 + clamp(DEX, -10, 10)
        self.HP = 1000 + clamp(HP, -1000, 1000)
        self.INV = 10 + clamp(INV, -10, 10)
        self.INT = 10 + clamp(INT, -10, 10)
        self.MR = 10 + clamp(MR, -10, 10)
        self.STR = 10 + clamp(STR, -10, 10)

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
            0, 1, -200, 0, -1, 0, 1))

class Goblin(Char):
    def __init__(self, name):
        super().__init__(name, "goblin", Stats(
            -1, 2, -600, 1, -3, -1, -3))

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

