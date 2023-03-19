#!/usr/bin/env python3

from copy import copy, deepcopy


__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Stats:
    def __init__(self, ARM, DEX, HP, INV, INT, MR, STR):
        self.ARM = ARM
        self.DEX = DEX
        self.HP = HP
        self.INV = INV
        self.INT = INT
        self.MR = MR
        self.STR = STR

class Char:
    name = "Greg"
    kin = "base"
    died = False

    stats = None
    base_stats = None

    target = None

    def __str__(self):
        return f'{self.name} the {self.kin}'
    def __init__(self, name, kin, stats):
        self.name = name
        self.kin = kin
        self.stats = stats
        self.base_stats = deepcopy(self.stats)

class Human(Char):
    def __init__(self, name):
        super().__init__(name, "human", Stats(
            4, 10, 10, 10, 10, 10, 10))

class Orc(Char):
    def __init__(self, name):
        super().__init__(name, "orc", Stats(
            5, 10, 10, 11, 8, 8, 12))

class Elf(Char):
    def __init__(self, name):
        super().__init__(name, "elf", Stats(
            4, 10, 10, 9, 10, 12, 9))

class Goblin(Char):
    def __init__(self, name):
        super().__init__(name, "goblin", Stats(
            3, 12, 4, 11, 7, 9, 9))

def die(c):
    t = type(c)
    if(issubtype(t, Stats)):
        c.HP = 0
        c.INV = 0
    elif(issubtype(t, Char)):
        die(c.stats)
        c.target = None
    elif(isanysubtype(t, list, tuple)):
        for ci in c:
            die(ci)
    else:
        return False
    return True

