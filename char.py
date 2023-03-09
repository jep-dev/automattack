#!/usr/bin/env python3

from copy import copy, deepcopy

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Stats:
    armor = 0
    dexterity = 0
    health = 0
    initiative = 0
    intelligence = 0
    mresistance = 0
    strength = 0
    def __str__(self):
        return (f'(ARM, DEX, HP, INV, INT, MR, STR) = '
                f'({self.armor}, {self.dexterity}, '
                f'{self.health}, {self.initiative}, '
                f'{self.intelligence}, {self.mresistance}, '
                f'{self.strength})')
    def __init__(self, armor, dexterity, health, initiative,
            intelligence, mresistance, strength):
        self.armor = armor
        self.dexterity = dexterity
        self.health = health
        self.initiative = initiative
        self.intelligence = intelligence
        self.mresistance = mresistance
        self.strength = strength

class Char:
    name = "Greg"
    species = "base"

    base_stats = None
    stats = None

    target = None

    def __str__(self):
        return f'{self.name} the {self.species}'
    def __init__(self, name, species, stats):
        self.name = name
        self.species = species
        self.base_stats = deepcopy(stats)
        self.stats = stats

class Human(Char):
    def __init__(self, name):
        super().__init__(name, "human", Stats(
            4, 10, 10, 10, 10, 10, 10))
        # .2, .5, .5, .5, .5, .5, .5))

class Orc(Char):
    def __init__(self, name):
        super().__init__(name, "orc", Stats(
            5, 10, 10, 11, 8, 8, 12))
        # .25, .5, .5, .55, .4, .4, .6))

class Elf(Char):
    def __init__(self, name):
        super().__init__(name, "elf", Stats(
                4, 10, 10, 9, 10, 12, 9))
        # .2, .5, .5, .45, .5, .6, .45))

