#!/usr/bin/env python3

from char import *
from random import random, randint

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def initiator(lhs, rhs):
    if(len(lhs) < 1 or len(rhs) < 1):
        return (-1, 0)

    m = 0
    n = 0
    for i in lhs:
        m = m + max(0, i.initiative)
    for j in rhs:
        n = n + max(0, j.initiative)

    p = random() * (m + n)
    if(m >= p):
        li = 0
        for i in lhs:
            k = max(0, i.initiative)
            p = p - k
            if(p <= 0):
                return (0, li)
            li = li + 1
        return (-1, 1)
    else:
        lj = 0
        p = p - m
        for j in rhs:
            k = max(0, j.initiative)
            p = p - k
            if(p <= 0):
                return (1, lj)
            lj = lj + 1
        return (-1, 2)


def die(c):
    c.strength = 0
    c.health = 0
    c.initiative = 0

def dead(c):
    return c.health == 0

def damage(src, dest):
    s = src.strength
    if(s <= 0):
        return False
    h = dest.health - s
    if(h <= 0):
        die(dest)
    else:
        dest.health = h
    return True


