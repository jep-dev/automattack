#!/usr/bin/env python3

from copy import copy, deepcopy


__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Stats:
    ARM = 0
    DEX = 0
    HP = 0
    INV = 0
    INT = 0
    MR = 0
    STR = 0
    def __str__(self):
        return (#f'(ARM, DEX, HP, INV, INT, MR, STR) = '
                f'Stats({self.ARM:.1f}, {self.DEX:.1f}, ' \
                f'{self.HP:.1f}, {self.INV:.1f}, ' \
                f'{self.INT:.1f}, {self.MR:.1f}, ' \
                f'{self.STR:.1f})')
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

    base_stats = None
    stats = None

    target = None

    def __str__(self):
        return f'{self.name} the {self.kin}'
    def __init__(self, name, kin, stats):
        self.name = name
        self.kin = kin
        self.base_stats = deepcopy(stats)
        self.stats = stats

class Human(Char):
    def __init__(self, name, living=True):
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
