#!/usr/bin/env python3

from char import *
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Group(list):
    def transform(self, f, *args):
        return [f(m, *args) for m in members]
    def filter(self, f, *args):
        return [m for m in members if f(m, *args)]
    def filterout(self, f, *args):
        return [m for m in members if not f(m, *args)]

def chars(c):
    out = Group()
    if(issubclass(type(c), list)):
        for ci in c:
            out.extend(chars(ci))
    elif(issubclass(type(c), tuple)):
        for ci in c:
            out.extend(chars(ci))
    #elif(issubclass(type(c), Char)):
    else:
        out.append(c)
    return out

def life(g):
    return [gi for g in chars(g) if gi != None and alive(gi)]
def death(g):
    return [gi for g in chars(g) if gi == None or dead(gi)]


class Team(Group):
    pass
