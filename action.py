#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Damage:
    MGD = 0 # Magical
    PCD = 0 # Piercing
    CRD = 0 # Crushing
    NTD = 0 # Natural
    def __init__(self, MGD, PCD, CRD, NTD):
        self.MGD = MGD
        self.PCD = PCD
        self.CRD = CRD
        self.NTD = NTD

class Action:
    DMG = None
    SUB = None
    OBJ = None
    def __init__(self, DMG = None, SUB = None, OBJ = None):
        super().__init__(self)
        self.TYPE = TYPE
