#!/usr/bin/env python3

from util import *
from char import *
from random import random, randint

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def die(c):
    s = c.stats
    s.health = 0
    s.initiative = 0
    s.intelligence = 0
    s.strength = 0

def dead(c):
    return c != None and c.stats.health <= 0
def alive(c):
    return not dead(c)

def cleanup(lhs, rhs):
    for d in filter(dead, lhs):
        #die(d)
        for li in lhs:
            if(li.target == d):
                li.target = None
    for d in filter(dead, rhs):
        #die(d)
        for rj in rhs:
            if(rj.target == d):
                rj.target = None
    lhs = filter(alive, lhs)
    rhs = filter(alive, rhs)

def initiator(lhs, rhs):
    cleanup(lhs, rhs)

    #if(len(lhs) < 1):
    #    return ()
    #if(len(rhs) < 1):
    #    return ()

    m = 0
    n = 0
    for x in lhs:
        m = m + max(0, x.stats.initiative)
    for y in rhs:
        n = n + max(0, y.stats.initiative)

    p = random() * (m + n)

    for x in lhs:
        k = max(0, x.stats.initiative)
        p = p - k
        if(p <= 0):
            return (0, x)

    for x in rhs:
        k = max(0, x.stats.initiative)
        p = p - k
        if(p <= 0):
            return (1, x)

    return ()



def damage(s, d):
    src = s.stats
    dest = d.stats
    h0 = src.health
    if(h0 <= 0):
        die(s)
        return 0
    h1 = dest.health
    if(h1 <= 0):
        die(d)
        return 0

    d0 = clamp(src.dexterity) # / 20.0
    i0 = clamp(src.initiative) # / 20.0
    s0 = clamp(src.strength) # / 20.0

    a1 = clamp(dest.armor) # / 20.0
    d1 = clamp(dest.dexterity) # / 20.0

    p0 = .6
    p1 = .8

    l = d0 * p0 + i0 * (1 - p0)
    r = a1 * p1 + d1 * (1 - p1)
    p0 = l # * .8
    p1 = random() * (l + r)
    if(p0 < p1):
        return 0

    #dmg = .25 * s0 * d0
    dmg = s0 * d0 / 20.0

    h1 = h1 - dmg
    if(h1 <= 0):
        s.target = None
        die(d)
    else:
        dest.health = h1
    return dmg


