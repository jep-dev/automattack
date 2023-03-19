#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Damage:
    def __init__(self, MGD, PCD, CRD, NTD):
        self.MGD = MGD # Magical
        self.PCD = PCD # Piercing
        self.CRD = CRD # Crushing
        self.NTD = NTD # Natural

class Action:
    def __init__(self, SUB = None, OBJ = None, ACT = None):
        self.SUB = SUB # Subject
        self.OBJ = OBJ # Object
        self.ACt = ACT # Action
