#!/usr/bin/env python3

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
    weight = 0
    def __init__(self, armor, dexterity, health, initiative,
            intelligence, mresistance, strength, weight):
        self.armor = armor
        self.dexterity = dexterity
        self.health = health
        self.initiative = initiative
        self.intelligence = intelligence
        self.mresistance = mresistance
        self.strength = strength
        self.weight = weight

class Char(Stats):
    name = "Greg"
    species = "base"
    def __init__(self, name, species, armor, dexterity, health,
            initiative, intelligence, mresistance, strength):
        super().__init__(armor, dexterity, health, initiative,
                intelligence, mresistance, strength, 10)
        self.name = name
        self.species = species
    def __str__(self):
        return f"{self.name} the {self.species}"

class Human(Char):
    def __init__(self, name):
        super().__init__(name, "human",
                10, 10, 10, 10, 10, 10, 10)

class Orc(Char):
    def __init__(self, name):
        super().__init__(name, "orc",
                10, 10, 10, 12, 8, 8, 12)

class Elf(Char):
    def __init__(self, name):
        super().__init__(name, "elf",
                10, 10, 10, 8, 12, 12, 8)
