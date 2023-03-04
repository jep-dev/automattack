#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Stats:
    dexterity = 1
    health = 1
    intelligence = 1
    strength = 1
    def __init__(self, dexterity, health, intelligence, strength):
        self.dexterity = dexterity
        self.health = health
        self.intelligence = intelligence
        self.strength = strength

class Char(Stats):
    name = "Greg"
    species = "gregoid"
    def __init__(self, name, species, dexterity, health, intelligence, strength):
        super().__init__(self, dexterity, health, intelligence, strength)
        self.name = name
        self.species = species
    def print_char(self):
        print(self.name, "the", self.species)

class Human(Char):
    def __init__(self, name):
        super().__init__(self, name, "human", 10, 10, 10, 10)

class Orc(Char):
    def __init__(self, name):
        super().__init__(self, name, "orc", 10, 8, 8, 14)

class Elf(Char):
    def __init__(self, name):
        super().__init__(self, name, "elf", 10, 8, 14, 8)

