#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Stats:
    health = 1
    def __init__(self, health):
        self.health = health

class Animate(Stats):
    armor = 1
    dexterity = 1
    intelligence = 1
    strength = 1
    mresistance = 1
    def __init__(self, armor, dexterity,
            health, intelligence, mresistance, strength):
        super().__init__(self, health)
        self.armor = armor
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.mresistance = mresistance
        self.strength = strength

class Inanimate(Stats):
    weight = 1
    def __init__(self, health, weight):
        super().__init__(self, health)
        self.weight = weight

class Char(Animate):
    name = "Greg"
    species = "gregoid"
    def __init__(self, name, species, armor, dexterity,
            health, intelligence, mresistance, strength):
        super().__init__(self, armor, dexterity, health,
                intelligence, mresistance, strength)
        self.name = name
        self.species = species
    def __str__(self):
        return f"{self.name} the {self.species}"

class Human(Char):
    def __init__(self, name):
        super().__init__(self, name, "human",
                10, 10, 10, 10, 10)

class Orc(Char):
    def __init__(self, name):
        super().__init__(self, name, "orc",
                10, 10, 8, 8, 14)

class Elf(Char):
    def __init__(self, name):
        super().__init__(self, name, "elf",
                10, 10, 8, 14, 8)
