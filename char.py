#!/usr/bin/env python3

from copy import copy, deepcopy
import importlib

from util import *
from math import *
from numeric import *

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

def kins():
    return {"elf": Elf, "goblin": Goblin,
            "human": Human, "orc": Orc}

def armor(c, s = 2):
    t = type(c)
    if(issubclass(t, Stats)):
        return hyperbolic(c.ARM, s, 20)
    if(issubclass(t, Char)):
        return armor(c.stats, s)
    return None

def health(c):
    t = type(c)
    if(issubclass(t, Stats)):
        return clamp(c.HP, 0, 1000)
    if(issubclass(t, Char)):
        return health(c.stats)
    return None

def intelligence(c):
    t = type(c)
    if(issubclass(t, Stats)):
        return clamp(c.INT, 0, 20)
    if(issubclass(t, Char)):
        return health(c.stats)
    return None

def dead(c):
    t = type(c)
    if(issubclass(t, Stats)):
        return health(c) <= 0 or intelligence(c) <= 0
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
        return True
    if(issubclass(t, Char)):
        die(c.stats)
        c.target = None
        return True
    if(issubclass(t, (list, tuple))):
        for ci in c:
            if(not die(ci)):
                return False
        return True
    return False

#def parse(line):
#    name = line[0]
#    kin = ""
#    cls = ""
#    kin = line[2].lower()
#    match kin in:
#        case "elf":
#            return Elf
#        case "goblin":
#            return Goblin
#        case "human":
#            out = Human
#        case "orc":
#            out = Orc
#        default:
#            return None


